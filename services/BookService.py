from datetime import datetime
from sqlite3 import IntegrityError

from orm.database import get_session
from orm.entity import Book, BookIssuance, Isbn, BookType

session = get_session()


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


# Функция для добавления книги
def add_book(title, author, release_date, num_pub, place_pub, publisher, page_count, genre, book_type, success_label):
    try:
        release_date = release_date.date().toPyDate()  # Преобразуем объект QDateTime в объект datetime
        book = Book(title=title, author=author, release_date=release_date, num_pub=num_pub, place_pub=place_pub,
                    publisher=publisher, page_count=page_count,  isbn=genre, book_type=book_type)
        session.add(book)
        session.commit()
        success_label.setText("Книга успешно добавлена")
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
    return session.query(Isbn).filter_by(id=genre_id).first().name


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


def get_all_genres():
    return session.query(Isbn).all()


def get_all_book_types():
    return session.query(BookType).all()
