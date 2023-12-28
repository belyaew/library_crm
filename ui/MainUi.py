from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


def show_welcome_window(login_widget):
    welcome_dialog = QDialog(login_widget)  # Устанавливаем родительское окно
    layout = QVBoxLayout(welcome_dialog)
    login = login_widget.login.text()

    label = QLabel('Добро пожаловать, {}!'.format(login))
    layout.addWidget(label)

    button1 = QPushButton('Список книг')
    button2 = QPushButton('Читатели')

    layout.addWidget(button1)
    layout.addWidget(button2)

    button1.clicked.connect(lambda: print("Кнопка 'Список книг' нажата"))
    button2.clicked.connect(lambda: print("Кнопка 'Читатели' нажата"))

    login_widget.hide()  # Скрываем окно LoginWidget
    welcome_dialog.exec_()  # Открываем окно welcome_dialog

    welcome_dialog.close()  # Закрываем окно welcome_dialog после выполнения всех операций

