from PySide6.QtWidgets import *

from screens.utils.image_button import ImageButton


class NavigationGrid(QWidget):
    def __init__(self, main_path, main_stack):
        super().__init__()
        self.main_stack = main_stack
        self.setFixedSize(500, 500 / 3 - 40)
        # Test QR Code picture
        qr_test = ImageButton(main_path + "/assets/images/qr_test", 500, self.handleTestClick, self)
        back_button = ImageButton(main_path + "/assets/images/qr_test", 500, self.handleBackButtonClick, self)
        next_button = ImageButton(main_path + "/assets/images/qr_test", 500, self.handleNextButtonClick, self)
        # Set navigation layout grid
        layout = QGridLayout()
        layout.addWidget(back_button, 0, 1)
        layout.addWidget(qr_test, 0, 2)
        layout.addWidget(next_button, 0, 3)

        self.setLayout(layout)

    def handleTestClick(self):
        print('Click!')

    def handleNextButtonClick(self):
        current_index = self.main_stack.currentIndex()
        max_index = self.main_stack.count() - 1

        if current_index == max_index:
            self.main_stack.setCurrentIndex(0)
        else:
            self.main_stack.setCurrentIndex(current_index + 1)

    def handleBackButtonClick(self):
        current_index = self.main_stack.currentIndex()
        max_index = self.main_stack.count() - 1

        if current_index == 0:
            self.main_stack.setCurrentIndex(max_index)
        else:
            self.main_stack.setCurrentIndex(current_index - 1)
