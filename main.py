from orm.TestData import fillTestData
from orm.database import create_tables, drop_tables
from ui.ui import create_ui


def main():
    create_ui()  # Запуск основного пользовательского интерфейса


if __name__ == "__main__":
    drop_tables()
    create_tables()
    fillTestData()
    main()

# Создание таблиц в базе данных, если они не существуют
create_tables()
