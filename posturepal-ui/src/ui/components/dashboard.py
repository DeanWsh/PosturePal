from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PosturePal Dashboard')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.title_label = QLabel('PosturePal Dashboard')
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        self.posture_info_label = QLabel('Current Posture: Good')
        self.posture_info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.posture_info_label)

        self.best_time_label = QLabel('Best Continuous Good Position Time: 0 seconds')
        self.best_time_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.best_time_label)

        self.remind_button = QPushButton('Remind Me')
        self.remind_button.clicked.connect(self.remind_user)
        layout.addWidget(self.remind_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def update_posture_info(self, posture_status, best_time):
        self.posture_info_label.setText(f'Current Posture: {posture_status}')
        self.best_time_label.setText(f'Best Continuous Good Position Time: {best_time} seconds')

    def remind_user(self):
        # Logic to remind the user about their posture
        pass