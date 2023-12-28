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


# Функции для работы с базой данных
def create_tables():
    # Создание таблиц, если они не существуют
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def get_session():
    # Получение сессии для работы с базой данных
    return Session()
