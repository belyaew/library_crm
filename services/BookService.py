from sqlite3 import IntegrityError

from orm.database import get_session
from orm.entity import Book
from datetime import datetime


# Функция для добавления книги
def add_book(title, author, category_id):
    session = get_session()
    try:
        book = Book(title=title, author=author, release_date = datetime.now(), book_type='Манга')
        session.add(book)
        session.commit()
        print("Book added successfully")
    except IntegrityError:
        session.rollback()
        print("Error: Invalid author_id or category_id")
    finally:
        session.close()
