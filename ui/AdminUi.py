from PyQt5.QtCore import QSize, QDate
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDateTimeEdit, QComboBox, QPushButton

from services.BookService import get_all_genres, get_all_book_types, add_book
from services.ReaderService import get_all_workers, get_all_positions, updete_position


def add_book_window(widget):
    reader_window = QDialog(widget)  # Устанавливаем родительское окно
    layout = QVBoxLayout(reader_window)

    reader_window.setFixedSize(QSize(1000, 1000))

    # Отображаем форму для добавления книги
    author_label = QLabel('ФИО автора:')
    layout.addWidget(author_label)

    author_edit = QLineEdit()
    layout.addWidget(author_edit)

    # Текстовое поле для ввода названия книги
    text_label = QLabel('Название книги:')
    layout.addWidget(text_label)
    title_edit = QLineEdit()
    layout.addWidget(title_edit)

    num_pub_label = QLabel('Номер издания :')
    layout.addWidget(num_pub_label)
    num_pub_edit = QLineEdit()
    layout.addWidget(num_pub_edit)

    place_pub_label = QLabel('Место издания:')
    layout.addWidget(place_pub_label)
    place_pub_edit = QLineEdit()
    layout.addWidget(place_pub_edit)

    publisher_label = QLabel('Издатель:')
    layout.addWidget(publisher_label)
    publisher_edit = QLineEdit()
    layout.addWidget(publisher_edit)

    release_date_label = QLabel('Год издания:')
    layout.addWidget(release_date_label)
    release_date_edit = QDateTimeEdit()
    release_date_edit.setDate(QDate.currentDate())
    layout.addWidget(release_date_edit)

    page_count_label = QLabel('Количество страниц:')
    layout.addWidget(page_count_label)
    page_count_edit = QLineEdit()
    layout.addWidget(page_count_edit)

    genres = get_all_genres()
    book_types = get_all_book_types()

    # Списки для выбора жанра и типа книги
    genre_combo = QComboBox()
    book_type_combo = QComboBox()

    # Добавляем все жанры в список
    genre_label = QLabel('ISBN:')
    layout.addWidget(genre_label)
    for genre in genres:
        genre_combo.addItem(genre.name, genre.id)  # Здесь второй аргумент - это данные, связанные с элементом
    layout.addWidget(genre_combo)

    # Добавляем все типы книг в список
    bt_label = QLabel('Тип книги:')
    layout.addWidget(bt_label)
    for book_type in book_types:
        book_type_combo.addItem(book_type.name,
                                book_type.id)  # Здесь второй аргумент - это данные, связанные с элементом
    layout.addWidget(book_type_combo)

    success_label = QLabel()
    layout.addWidget(success_label)
    # Кнопка для добавления книги
    button = QPushButton('Добавить')
    button.clicked.connect(lambda: add_book(
        title_edit.text(),
        author_edit.text(),
        release_date_edit,
        num_pub_edit.text(),
        place_pub_edit.text(),
        publisher_edit.text(),
        page_count_edit.text(),
        genres[genre_combo.currentIndex()].id,  # Получаем ID выбранного жанра
        book_types[book_type_combo.currentIndex()].id,# Получаем ID выбранного типа книги
        success_label
    ))
    layout.addWidget(button)

    # Добавляем кнопку для закрытия окна
    buttonClose = QPushButton('Закрыть')
    from ui.MainUi import show_welcome_window
    buttonClose.clicked.connect(lambda: show_welcome_window(reader_window))
    layout.addWidget(buttonClose)

    widget.hide()
    reader_window.exec_()  # Открываем окно book_dialog


def change_worker_posision_window(widget):
    reader_window = QDialog(widget)  # Устанавливаем родительское окно
    layout = QVBoxLayout(reader_window)

    reader_window.setFixedSize(QSize(200, 180))

    workers = get_all_workers()
    bt_label = QLabel('Выберите сотрудника:')
    layout.addWidget(bt_label)

    worker_combo = QComboBox()
    for worker in workers:
        fio = worker.last_name + ' ' + worker.first_name
        worker_combo.addItem(fio, worker.id)  # Здесь второй аргумент - это данные, связанные с элементом
    layout.addWidget(worker_combo)

    positions = get_all_positions()
    bt_label = QLabel('Выберите новую роль сотрудника:')
    layout.addWidget(bt_label)

    position_combo = QComboBox()
    for position in positions:
        position_combo.addItem(position.position,
                               position.id)  # Здесь второй аргумент - это данные, связанные с элементом
    layout.addWidget(position_combo)

    button = QPushButton('Изменить роль')

    success_label = QLabel()
    layout.addWidget(success_label)
    button.clicked.connect(lambda: updete_position(
        workers[worker_combo.currentIndex()],
        positions[position_combo.currentIndex()],
        success_label
    ))
    layout.addWidget(button)

    # Добавляем кнопку для закрытия окна
    buttonClose = QPushButton('Закрыть')
    from ui.MainUi import show_welcome_window
    buttonClose.clicked.connect(lambda: show_welcome_window(reader_window))
    layout.addWidget(buttonClose)

    widget.hide()
    reader_window.exec_()  # Открываем окно book_dialog
