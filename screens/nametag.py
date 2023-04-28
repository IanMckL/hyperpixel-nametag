from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from screens.utils.image_button import ImageButton
from screens.utils.navigation_grid import NavigationGrid
from screens.utils.text_box import TextBox


class Nametag(QWidget):
    def __init__(self, main_path, main_stack, name, title, logo_name=None):
        super().__init__()
        layout = QVBoxLayout()

        # Add logo if logo_path exists
        if logo_name:
            logo_button = ImageButton(main_path + f'/assets/images/{logo_name}', 500)

            logo_container = QHBoxLayout()
            logo_container.addWidget(logo_button)

            logo_widget = QWidget()
            logo_widget.setContentsMargins(0, 0, 0, 0)
            logo_widget.setLayout(logo_container)

            self.logo = logo_widget

        self.name_label = TextBox(main_path, f'{name}', size=70)
        self.title_label = TextBox(main_path, f'{title}', size=40)
        self.navigation = NavigationGrid(main_path, main_stack)

        layout.addWidget(self.name_label)
        if logo_name:
            layout.addWidget(self.logo)
        layout.addWidget(self.title_label)
        layout.addWidget(self.navigation)
        layout.setSpacing(0)

        self.setLayout(layout)
