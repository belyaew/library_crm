from sqlite3 import IntegrityError

from orm.database import get_session
from orm.entity import Book, BookIssuance, Genre, BookType
from datetime import datetime

session = get_session()


# Функция для добавления книги
def add_book(title, author, category_id):
    try:
        book = Book(title=title, author=author, release_date=datetime.now(), book_type='Манга')
        session.add(book)
        session.commit()
        print("Book added successfully")
    except IntegrityError:
        session.rollback()
        print("Error: Invalid author_id or category_id")
    finally:
        session.close()


def get_issuance_records():
    try:
        return session.query(BookIssuance).filter(BookIssuance.return_date.is_(None) |
                                                  (BookIssuance.return_date < datetime.now())).all()
    finally:
        session.commit()


def get_all_books():
    return session.query(Book).all()


def get_genre_by_id(genre_id):
    return session.query(Genre).filter_by(id=genre_id).first().name


def get_book_type(book_type_id):
    return session.query(BookType).filter_by(id=book_type_id).first().name


def issuance_book(book_id, reader_id, worker_id, library_address_id):
    try:
        book = BookIssuance(book_id=book_id, reader_id=reader_id, issue_date=datetime.now(), worker_id=worker_id,
                            library_address_id=library_address_id)
        session.add(book)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise RuntimeError("Ошибка при выдачи книги")
    finally:
        session.close()
