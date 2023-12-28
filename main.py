from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from orm.database import create_tables, drop_tables
from ui.ui import create_ui


def main():
    create_ui()  # Запуск основного пользовательского интерфейса


if __name__ == "__main__":
    # drop_tables()
    create_tables()
    main()

# Создание таблиц в базе данных, если они не существуют
create_tables()