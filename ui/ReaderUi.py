from datetime import datetime

from PyQt5.QtCore import QSize, QDate
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QListWidget, QWidget, QHBoxLayout, QLabel, QPushButton, \
    QListWidgetItem, QComboBox, QDateEdit

from services.ReaderService import get_all_readers, get_all_subscriptions, handle_add_subscription, update_subscription


def show_reader_window(widget):
    global reader_window
    if 'reader_window' in globals():  # проверяем, существует ли уже окно book_dialog
        reader_window.close()
    reader_window = QDialog(widget)  # Устанавливаем родительское окно
    layout = QVBoxLayout(reader_window)

    reader_window.setFixedSize(QSize(900, 900))

    # Получаем список пользователей из базы данных
    readers = get_all_readers()
    subscriptions = get_all_subscriptions()

    # Отображаем список пользователей в QListWidget
    reader_list_widget = QListWidget()

    for reader in readers:
        reader_widget = QWidget()
        reader_layout = QHBoxLayout(reader_widget)

        reader_label = QLabel(f"{reader.first_name} | {reader.last_name} | {reader.birth_date} | {reader.email} |"
                              f" {reader.address}")

        reader_layout.addWidget(reader_label)

        sub = get_subscription_by_reader_id(reader.id, subscriptions)
        hasSub = sub is None

        if hasSub:
            issue_button = QPushButton('Оформить подписку')
            issue_button.setStyleSheet("color: red;")
            issue_button.clicked.connect(lambda checked, r=reader: make_a_sub(r, None))
            reader_layout.addWidget(issue_button)
        else:
            if sub.expiration_date < datetime.now():
                issue_button = QPushButton('Продлить подписку')
                issue_button.setStyleSheet("color: red;")
                issue_button.clicked.connect(lambda checked, r=reader, s=sub: make_a_sub(r, s))
                reader_layout.addWidget(issue_button)
            else:
                issued_label = QLabel(f"{sub.subscription_type} До {sub.expiration_date.date()}")
                issued_label.setStyleSheet("color: green;")
                reader_layout.addWidget(issued_label)

        # Устанавливаем пользовательский виджет в QListWidgetItem
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 60))  # Устанавливаем размер строки
        reader_list_widget.addItem(item)
        reader_list_widget.setItemWidget(item, reader_widget)

    layout.addWidget(reader_list_widget)

    # Добавляем кнопку для закрытия окна
    button1 = QPushButton('Закрыть')
    from ui.MainUi import show_welcome_window
    button1.clicked.connect(lambda: show_welcome_window(reader_window))
    layout.addWidget(button1)

    widget.hide()
    reader_window.exec_()  # Открываем окно book_dialog


def make_a_sub(reader, sub):
    reader_dialog = QDialog()  # Создаем новое окно
    layout = QVBoxLayout(reader_dialog)

    # Устанавливаем размеры главного окна
    reader_dialog.setFixedSize(QSize(300, 130))

    label = QLabel('Добавить подписку для пользователя: {}'.format(reader.last_name))
    layout.addWidget(label)

    # Создаем выпадающий список для выбора типа подписки
    subscription_type_combo = QComboBox()
    subscription_type_combo.addItem("Ежемесячная", "Ежемесячная")
    subscription_type_combo.addItem("Ежегодная", "Ежегодная")
    layout.addWidget(subscription_type_combo)

    # Создаем виджет даты для выбора даты подписки
    expiration_date = QDateEdit()
    expiration_date.setDate(QDate.currentDate())
    expiration_date.setMinimumDate(QDate.currentDate())
    layout.addWidget(expiration_date)

    # Создаем кнопку для добавления подписки
    add_subscription_button = QPushButton("Добавить подписку")

    # Подключаем сигнал нажатия кнопки для добавления подписки
    add_subscription_button.clicked.connect(
        lambda: handle_add_subscription_internal(reader, subscription_type_combo, expiration_date.date(),
                                                 reader_dialog, sub))
    layout.addWidget(add_subscription_button)

    reader_dialog.exec_()


def handle_add_subscription_internal(reader, subscription_type, expiration_date, reader_dialog, sub):
    if sub is None:
        handle_add_subscription(reader, subscription_type, expiration_date)
    else:
        update_subscription(reader, subscription_type, expiration_date, sub)
    show_reader_window(reader_dialog)


def get_subscription_by_reader_id(reader_id, subscriptions):
    for subscription in subscriptions:
        if subscription.reader_id == reader_id:
            return subscription
    return None
