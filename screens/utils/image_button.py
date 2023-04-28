from PySide6.QtGui import QPixmap, QMouseEvent, Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class ImageButton(QWidget):
    def __init__(self, image_path, central_height, on_click=None, parent=None):
        super().__init__()
        self.on_click = on_click

        # Create QLabel widget to hold the image
        self.image_label = QLabel("")
        self.image_label.setScaledContents(True)  # Scale the image to fit the label
        self.setFixedSize(central_height / 3 - 40, central_height / 3 - 40)

        try:
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
        except Exception as e:
            print(f"Error loading image: {e}")

        # Create a layout for the widget
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # Trigger on_click function if one is provided
        if event.button() in (Qt.LeftButton, Qt.RightButton) and self.on_click:
            try:
                self.on_click()
            except Exception as e:
                print(f"Error completing mouse press event: {e}")
        # Handle case for no function provided
        else:
            print('Nothing to do!')
