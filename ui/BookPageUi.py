from datetime import datetime

from PyQt5.QtCore import QSize, QDateTime, QDate
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QMessageBox, \
    QWidget, QHBoxLayout, QDateEdit

from orm.database import get_session, issue_book

from services.BookService import get_issuance_records, get_all_books, get_book_type, get_genre_by_id, issuance_book
from services.ReaderService import get_all_readers
from services.UserServise import get_lib_name_by_login


def show_books_window(widget):
    book_dialog = QDialog(widget)  # Устанавливаем родительское окно
    layout = QVBoxLayout(book_dialog)

    book_dialog.setFixedSize(QSize(1600, 1600))

    label = QLabel('Список книг для пользователя: {}'.format(widget.login.text()))
    layout.addWidget(label)

    # Получаем список книг из базы данных
    books = get_all_books()

    # Загружаем информацию о выдаче книг из базы данных
    issuance_records = get_issuance_records()

    # Отображаем список книг в QListWidget
    book_list_widget = QListWidget()
    for book in books:
        book_widget = QWidget()
        book_layout = QHBoxLayout(book_widget)

        # Добавляем название книги и автора
        book_label = QLabel(f"{book.title} | {book.author} | {book.release_date} | {get_genre_by_id(book.genre)} |"
                            f" {get_book_type(book.book_type)}")
        book_layout.addWidget(book_label)

        if book.id not in [record.book_id for record in issuance_records]:
            issued_label = QLabel('Выдано')
            issued_label.setStyleSheet("color: red;")
            book_layout.addWidget(issued_label)
        else:
            issue_button = QPushButton('Выдать')
            issue_button.clicked.connect(lambda: show_issuance_book_window(book))
            book_layout.addWidget(issue_button)

        # Устанавливаем пользовательский виджет в QListWidgetItem
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 60))  # Устанавливаем размер строки
        book_list_widget.addItem(item)
        book_list_widget.setItemWidget(item, book_widget)

    layout.addWidget(book_list_widget)

    # Добавляем кнопку для закрытия окна
    button1 = QPushButton('Закрыть')
    button1.clicked.connect(book_dialog.close)
    layout.addWidget(button1)

    widget.hide()
    book_dialog.exec_()  # Открываем окно book_dialog


def show_issuance_book_window(book):
    book_dialog = QDialog()  # Создаем новое окно
    layout = QVBoxLayout(book_dialog)

    # Устанавливаем размеры главного окна
    book_dialog.setFixedSize(QSize(800, 600))

    # Получаем список пользователей из базы данных
    readers = get_all_readers()

    # Отображаем данные книги
    label = QLabel(f"{book.title} | {book.author} | {book.release_date} | {get_genre_by_id(book.genre)} |"
                            f" {get_book_type(book.book_type)}")
    layout.addWidget(label)

    # Отображаем список пользователей
    user_list_widget = QListWidget()
    for reader in readers:
        user_widget = QWidget()
        user_layout = QHBoxLayout(user_widget)

        # Добавляем имя пользователя
        user_label = QLabel(f"{reader.first_name} | {reader.last_name} | {reader.birth_date} | {reader.email} | {reader.address}")
        user_layout.addWidget(user_label)

        # Устанавливаем пользовательский виджет в QListWidgetItem
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 60))  # Устанавливаем размер строки
        user_list_widget.addItem(item)
        user_list_widget.setItemWidget(item, user_widget)

    layout.addWidget(user_list_widget)

    # Добавляем поле для выбора даты
    date_edit = QDateEdit()
    layout.addWidget(date_edit)
    date_edit.setDate(QDate.currentDate())
    # Устанавливаем минимальную дату в текущую дату
    date_edit.setMinimumDate(QDate.currentDate())

    # Добавляем кнопку "Выдать"
    issue_button = QPushButton('Выдать')
    issue_button.clicked.connect(lambda: issuance_book_internal())
    layout.addWidget(issue_button)

    book_dialog.exec_()

    def issuance_book_internal():
        from ui.MainUi import login
        issuance_book(book.id, reader.id, login, get_lib_name_by_login(login))
        show_books_window(book_dialog)

