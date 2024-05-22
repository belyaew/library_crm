from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

from services.AuthService import check_credentials
from ui.MainUi import show_welcome_window


class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        self.label = QLabel('Введите имя пользователя:')
        self.login = QLineEdit()
        self.password_line_edit = QLineEdit()
        self.push_button = QPushButton('Проверить')

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.login)
        self.layout.addWidget(self.password_line_edit)
        self.layout.addWidget(self.push_button)

        # Заменяем введённый логин на звездочки в UI
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        # Для нажатия enter
        self.login.returnPressed.connect(self.check_credentials_internal)
        self.password_line_edit.returnPressed.connect(self.check_credentials_internal)

        self.push_button.clicked.connect(self.check_credentials_internal)

        self.setLayout(self.layout)
        self.setFixedSize(QSize(300, 140))

    def check_credentials_internal(self):
        result = check_credentials(self.login.text(), self.password_line_edit.text())
        if result:
            show_welcome_window(self)
        else:
            self.push_button.setText('Неверные учетные данные')
            self.push_button.setStyleSheet("color: red;")
