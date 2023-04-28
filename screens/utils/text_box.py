from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout


class TextBox(QWidget):
    def __init__(self, main_path, text, font_name="banhof", size=40):
        super().__init__()

        self.text = QLabel(f'{text}')

        font_id = QFontDatabase.addApplicationFont(main_path + f'/assets/fonts/{font_name}.ttf')
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        self.text.setFont(QFont(font_family, size))
        self.text.setStyleSheet('color: white;')
        self.text.setAlignment(Qt.AlignCenter)

        layout = QHBoxLayout()
        layout.addWidget(self.text)

        self.setLayout(layout)
