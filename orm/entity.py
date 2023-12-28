from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from orm.database import Base


# Таблица "Книги"
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    author = Column(String)
    release_date = Column(DateTime)
    genre = ForeignKey('genres.id')
    book_type = Column(String)  # например, "твердый переплет", "мягкий переплет", "комиксы", "манга"


# Таблица "Читатели"
class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(DateTime)
    email = Column(String(120), index=True, unique=True)
    address = Column(String)


# Таблица "Выданные книги"
class BookIssuance(Base):
    __tablename__ = 'book_issuance'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    reader_id = Column(Integer, ForeignKey('readers.id'))
    issue_date = Column(DateTime, default=datetime.now)
    return_date = Column(DateTime)
    worker_id = Column(Integer, ForeignKey('worker.id'))
    library_address_id = Column(Integer, ForeignKey('library_addresses.id'))

    book = relationship("Book")
    reader = relationship("Reader")
    worker = relationship("Worker")
    library_address = relationship("LibraryAddress")


# Таблица "Работники"
class Worker(Base):
    __tablename__ = 'worker'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    hire_date = Column(DateTime)
    position = Column(String)


# Таблица "Адрес библиотеки"
class LibraryAddress(Base):
    __tablename__ = 'library_addresses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    address = Column(String)


# Таблица "Жанр"
class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)


# Таблица "Позиция работника"
class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String)


# Таблица "Подписки"
class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    reader_id = Column(Integer, ForeignKey('readers.id'))
    subscription_type = Column(String)  # например, "ежемесячная", "ежегодная"
    expiration_date = Column(DateTime)

    reader = relationship("Reader")


class BookType(Base):
    __tablename__ = 'book_types'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book")


class Auth(Base):
    __tablename__ = 'auth'
    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey('worker.id'))
    login = Column(String)
    # todo Сделать шифратор
    password = Column(String)



