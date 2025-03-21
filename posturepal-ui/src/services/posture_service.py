import requests
import json

class PostureService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1"

    def get_posture_feedback(self, image_data, head_angles, best_time):
        roll, pitch = head_angles
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        prompt = self._create_prompt(roll, pitch, best_time)

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 150,
            "temperature": 1.3,
        }

        response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            print("Error:", response.json())
            return None

    def _create_prompt(self, roll, pitch, best_time):
        return f"You are PosturePal, a friendly assistant that detects the user's sitting posture. " \
            f"The head roll is {roll:.2f} degrees and the head pitch is {pitch:.2f} degrees. " \
            f"The best time the user has maintained a good position is {best_time} seconds. " \
            f"Provide feedback in a humorous and encouraging way."