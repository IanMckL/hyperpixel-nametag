from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class ImageButton(QWidget):
    def __init__(self, image_path, central_height, parent=None):
        super().__init__()

        # Create QLabel widget to hold the image
        self.image_label = QLabel("")
        self.image_label.setScaledContents(True)  # Scale the image to fit the label
        self.setFixedSize(central_height / 3 - 40, central_height / 3 - 40)

        # Load the image and set it as the pixmap for the label
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)

        # Create a layout for the widget
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)
