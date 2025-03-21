import flet as ft
import cv2
import threading
import time
import posenet
import torch
from posenet.utils import read_cap
from posenet.resnet import get_resnet

# Global variables to control the posture detection loop
running = False
start_time = 0
roll_history = []
pitch_history = []
good_position_time = 0
best_time = 0
last_time = time.time()

def main(page: ft.Page):
    page.title = "PosturePal"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50
    page.bgcolor = ft.colors.BLUE_GREY_100

    # Initialize camera and models
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    model = posenet.load_model(6969)
    resnet = get_resnet(180)
    output_stride = model.output_stride

    # UI components
    start_button = ft.ElevatedButton(text="Start Detection", on_click=lambda e: start_detection())
    stop_button = ft.ElevatedButton(text="Stop Detection", on_click=lambda e: stop_detection(), disabled=True)
    image = ft.Image(src="images/placeholder.png", width=640, height=480)
    roll_text = ft.Text("Roll: 0.0°", size=20, color=ft.colors.BLACK)
    pitch_text = ft.Text("Pitch: 0.0°", size=20, color=ft.colors.BLACK)
    best_time_text = ft.Text("Best Time: 0.0s", size=20, color=ft.colors.BLACK)

    def update_ui(image_src, roll, pitch, best_time):
        image.src = image_src
        roll_text.value = f"Roll: {roll:.2f}°"
        pitch_text.value = f"Pitch: {pitch:.2f}°"
        best_time_text.value = f"Best Time: {best_time:.2f}s"
        page.update()

    def start_detection():
        global running
        running = True
        start_button.disabled = True
        stop_button.disabled = False
        page.update()
        threading.Thread(target=detect_posture).start()

    def stop_detection():
        global running
        running = False
        start_button.disabled = False
        stop_button.disabled = True
        page.update()

    def detect_posture():
        global roll_history, pitch_history, good_position_time, best_time, last_time
        start_time = time.time()
        frame_count = 0

        while running:
            input_image_raw, display_image, output_scale = read_cap(
                cap, scale_factor=0.2, output_stride=output_stride)

            with torch.no_grad():
                input_image = torch.Tensor(input_image_raw)
                input_image = (input_image + 1) / 2

                heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = model(input_image)

                pose_scores, keypoint_scores, keypoint_coords, _ = posenet.decode_multiple_poses(
                    heatmaps_result.squeeze(0),
                    offsets_result.squeeze(0),
                    displacement_fwd_result.squeeze(0),
                    displacement_bwd_result.squeeze(0),
                    output_stride=output_stride,
                    max_pose_detections=10,
                    min_pose_score=0.2)

            for pi, (pose_score, keypoint_score, keypoint_coord) in enumerate(zip(pose_scores, keypoint_scores, keypoint_coords)):
                if pose_score > 0.15:
                    with torch.no_grad():
                        roll, pitch = resnet(input_image, keypoint_coord)
                    roll_history.append(roll)
                    pitch_history.append(pitch)

            if frame_count % 10 == 0 and frame_count != 0:
                average_roll = sum(roll_history[-10:]) / 10
                average_pitch = sum(pitch_history[-10:]) / 10

                if average_roll <= 20 and average_roll >= -20 and average_pitch <= 10 and average_pitch >= -10:
                    good_position_time += time.time() - last_time
                    best_time = max(best_time, good_position_time)
                else:
                    good_position_time = 0

                last_time = time.time()
                update_ui("images/placeholder.png", average_roll, average_pitch, best_time)

            frame_count += 1

        cap.release()

    page.add(
        ft.Column(
            [
                image,
                roll_text,
                pitch_text,
                best_time_text,
                ft.Row([start_button, stop_button], alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)