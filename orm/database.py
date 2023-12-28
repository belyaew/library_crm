from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание подключения к базе данных
# Подставить свой коннект к бд
# engine = create_engine('jdbc:postgresql://localhost:5433/library_crm')
engine = create_engine('postgresql://user:admin@localhost:5433/library_crm')
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)


# Функция для выдачи книги читателю
def issue_book(book_id, reader_id, return_date):
    session = get_session()
    try:
        from orm.entity import BookIssuance
        issuance = BookIssuance(book_id=book_id, reader_id=reader_id, return_date=return_date)
        session.add(issuance)
        session.commit()
        print("Book issued successfully")
    except Exception as e:
        print("Error issuing the book:", e)
        session.rollback()
    finally:
        session.close()


# Функции для работы с базой данных
def create_tables():
    # Создание таблиц, если они не существуют
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def get_session():
    # Получение сессии для работы с базой данных
    return Session()
