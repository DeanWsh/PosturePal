from tkinter import Tk, Label, Button, Entry, StringVar, Frame

class SettingsComponent:
    def __init__(self, master):
        self.master = master
        self.master.title("Settings")
        
        self.frame = Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.camera_id_var = StringVar()
        self.camera_width_var = StringVar()
        self.camera_height_var = StringVar()
        self.remind_interval_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        Label(self.frame, text="Camera ID:").grid(row=0, column=0, sticky="w")
        Entry(self.frame, textvariable=self.camera_id_var).grid(row=0, column=1)

        Label(self.frame, text="Camera Width:").grid(row=1, column=0, sticky="w")
        Entry(self.frame, textvariable=self.camera_width_var).grid(row=1, column=1)

        Label(self.frame, text="Camera Height:").grid(row=2, column=0, sticky="w")
        Entry(self.frame, textvariable=self.camera_height_var).grid(row=2, column=1)

        Label(self.frame, text="Reminder Interval (seconds):").grid(row=3, column=0, sticky="w")
        Entry(self.frame, textvariable=self.remind_interval_var).grid(row=3, column=1)

        Button(self.frame, text="Save Settings", command=self.save_settings).grid(row=4, columnspan=2)

    def save_settings(self):
        camera_id = self.camera_id_var.get()
        camera_width = self.camera_width_var.get()
        camera_height = self.camera_height_var.get()
        remind_interval = self.remind_interval_var.get()

        # Here you would typically save these settings to a config file or apply them to the application
        print(f"Settings saved: Camera ID={camera_id}, Width={camera_width}, Height={camera_height}, Reminder Interval={remind_interval}")

def main():
    root = Tk()
    settings_component = SettingsComponent(root)
    root.mainloop()

if __name__ == "__main__":
    main()