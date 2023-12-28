from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

from services.UserServise import get_position_by_login
from ui.AdminUi import add_book_window
from ui.BookPageUi import show_books_window
from ui.ReaderUi import show_reader_window

global login
def show_welcome_window(login_widget):
    welcome_dialog = QDialog(login_widget)  # Устанавливаем родительское окно
    layout = QVBoxLayout(welcome_dialog)

    welcome_dialog.setFixedSize(QSize(450, 200))
    global login
    if 'login' not in globals():
        login = login_widget.login.text()

    label = QLabel('Добро пожаловать, {}!'.format(login))
    layout.addWidget(label)

    button1 = QPushButton('Список книг')
    button2 = QPushButton('Читатели')

    position = get_position_by_login(login)
    if position == 'Администратор':
        button3 = QPushButton('Добавить книги')
        button4 = QPushButton('Изменить роль сотрудника')
        layout.addWidget(button4)
        layout.addWidget(button3)
        button3.clicked.connect(lambda: add_book_window(login_widget))
        button4.clicked.connect(lambda: show_reader_window(login_widget))

    layout.addWidget(button1)
    layout.addWidget(button2)


    button1.clicked.connect(lambda: show_books_window(login_widget))
    button2.clicked.connect(lambda: show_reader_window(login_widget))


    login_widget.hide()  # Скрываем окно LoginWidget
    welcome_dialog.exec_()  # Открываем окно welcome_dialog

    welcome_dialog.close()  # Закрываем окно welcome_dialog после выполнения всех операций

