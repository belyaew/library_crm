import random
from random import choice

from orm.database import get_session
from orm.entity import Reader, Book, BookIssuance, Worker, LibraryAddress, Isbn, BookType, Auth, Subscription, Position


def fillTestData():
    session = get_session()
    workers = []
    libraryAdresses = []
    bookTypes = []
    positions = []
    readers = []
    try:

        # Позиция работника
        for i in ['Администратор', 'Менеджер', 'Библиотекарь']:
            if i == 0:
                position_choise = 'Администратор'
            else:
                position_choise = i
            position = Position(position=position_choise)
            positions.append(position)
            session.add(position)

        # BookType
        btypes = ['Печатная', 'Электронная']
        for bt in btypes:
            bookType = BookType(name=bt)
            session.add(bookType)
            bookTypes.append(bookType)
            session.commit()

        # Адрес библиотеки
        for i in range(5):
            name = choice(['Центральная', 'Перспективная', 'Слободская', 'Транспортная'])
            city = choice(['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'])
            address = choice([
                'Улица Ленина, дом 1', 'Улица Пушкина, дом 10', 'Улица Горького, дом 5', 'Улица Советская, дом 25'])
            libraryAdress = LibraryAddress(name=name, city=city, address=address)
            libraryAdresses.append(libraryAdress)
            session.add(libraryAdress)
            session.commit()

        # Работники
        for i in range(2):
            if i == 0:
                pos = 1
            else:
                pos = random.choice(positions).id
            first_name = choice(['Иван', 'Алексей', 'Александр'])
            last_name = choice(['Иванов', 'Петров', 'Сидоров', 'Смирнов'])
            hire_date = choice([
                '2020-01-01', '2020-02-15', '2020-03-10', '2020-04-25', '2020-05-12',
                '2020-06-26', '2020-07-13', '2020-08-28', '2020-09-15', '2020-10-03'])
            worker = Worker(first_name=first_name, last_name=last_name, hire_date=hire_date,
                            position=pos, lib_adress=random.choice(libraryAdresses).id)
            workers.append(worker)
            session.add(worker)
            session.commit()  # Committing here to ensure that worker.id is set

        # Читатели
        for i in range(10):
            first_name = choice(['Иван', 'Мария', 'Алексей', 'Елена'])
            last_name = choice(['Иванов', 'Петрова', 'Сидоров', 'Смирнова'])
            birth_date = choice([
                '1990-01-01', '1991-02-15', '1992-03-10', '1993-04-25', '1994-05-12',
                '1995-06-26', '1996-07-13', '1997-08-28', '1998-09-15', '1999-10-03'])
            email = f"reader{i}@example.com"
            address = f"Улица {choice(['Центральная', 'Перспективная', 'Слободская', 'Транспортная'])} {choice(['дом 1', 'дом 5', 'дом 10', 'дом 25'])}"
            reader = Reader(first_name=first_name, last_name=last_name, birth_date=birth_date, email=email,
                            address=address)
            readers.append(reader)
            session.add(reader)
            session.commit()

        # Жанр
        isbns = ['979-5-9222-0976-3', '978-5-9221-0979-5', '978-5-7038-3447-4', '5-87210-056-6', '5-271-01118-7']
        isbns_entity = []
        for isbn in isbns:
            create_isbns = Isbn(name=isbn)
            isbns_entity.append(create_isbns)
            session.add(create_isbns)
            session.commit()

        # Книги
        # for i in range(50):
        #     title = choice(['Книга 1', 'Книга 2', 'Книга 3', 'Книга 4', 'Книга 5'])
        #     author = choice(['Автор 1', 'Автор 2', 'Автор 3', 'Автор 4', 'Автор 5'])
        #     release_date = choice([
        #         '2020-01-01', '2020-02-15', '2020-03-10', '2020-04-25', '2020-05-12',
        #         '2020-06-26', '2020-07-13', '2020-08-28', '2020-09-15', '2020-10-03'])
        #     isbn_id = choice([i for i in range(1, 6)])
        #     session.add(Book(title=title, author=author, release_date=release_date, isbn=isbn_id,
        #                      book_type=random.choice(bookTypes).id))

        session.add(Book(title='Сборник задач по линейной алгебре: учебник для вузов',
                         author='И.В. Проскуряков',
                         num_pub='Издание 7е',
                         place_pub='"Наука" главная редакция физико-математической литературы',
                         release_date='1984',
                         publisher='Москва',
                         page_count='336',
                         isbn=isbns_entity[0].id,
                         book_type=bookTypes[0].id))

        session.add(Book(title='Курс аналитической геометрии и линейной алгебры:учебник для вузов',
                         author='Д.В. Беклемишев',
                         num_pub='Издание 12е',
                         place_pub='ФИЗМАЛИТ',
                         release_date='2008',
                         publisher='Москва',
                         page_count='312',
                         isbn=isbns_entity[1].id,
                         book_type=bookTypes[0].id))

        session.add(Book(title='Учебник английского языка для студентов',
                         author='И.В. Орловская',
                         num_pub='Издание 11е',
                         place_pub='Издательство МГТУ им Баумана',
                         release_date='2010',
                         publisher='Москва',
                         page_count='447',
                         isbn=isbns_entity[2].id,
                         book_type=bookTypes[0].id))

        session.add(Book(title='Россия в мировой истории',
                         author='В.С. Порохня',
                         num_pub='Издание 1е',
                         place_pub='Издательство МАИ',
                         release_date='2003',
                         publisher='Смоленск',
                         page_count='464',
                         isbn=isbns_entity[3].id,
                         book_type=bookTypes[0].id))

        session.add(Book(title='Задачи и упражнения по математическому анализу: учебник для вузов',
                         author='Б. П. Демидович',
                         num_pub='Издание 1е',
                         place_pub='Издательство Астрель',
                         release_date='2001',
                         publisher='Москва',
                         page_count='495',
                         isbn=isbns_entity[4].id,
                         book_type=bookTypes[0].id))

        session.commit()

        # Выданные книги
        for i in range(20):
            # book_id = choice([i for i in range(1, 1)])  #ПОМЕНЯТЬ НА 6!!!!!!!
            book_id = 1  #ПОМЕНЯТЬ НА 6!!!!!!!
            reader_id = random.choice(readers).id
            issue_date = choice([
                '2020-01-01', '2020-02-15', '2020-03-10', '2020-04-25', '2020-05-12',
                '2020-06-26', '2020-07-13', '2020-08-28', '2020-09-15', '2020-10-03'])
            return_date = choice([
                '2023-01-01', '2020-02-15', '2020-03-10', None])
            session.add(
                BookIssuance(book_id=book_id, reader_id=reader_id, issue_date=issue_date, return_date=return_date,
                             library_address_id=random.choice(libraryAdresses).id, worker_id=random.choice(workers).id))

        # Подписки
        for i in range(10):
            subscription_type = choice(['ежемесячная', 'ежегодная'])
            expiration_date = choice([
                '2020-01-01', '2021-02-15', '2022-03-10', '2024-04-25', '2025-05-12'])
            session.add(Subscription(subscription_type=subscription_type, expiration_date=expiration_date,
                                     reader_id=random.choice(readers).id))

        # Создаем учётные записи и связываем их с работниками
        for worker in workers:
            login = f"{worker.first_name.lower()}.{worker.last_name.lower()}@example.com"
            password = "password"
            auth = Auth(worker_id=worker.id, login=login, password=password)
            session.add(auth)

        session.add(Auth(worker_id=1, login="a", password="a"))
        session.add(Auth(worker_id=1, login="ф", password="ф"))
        session.commit()
    except Exception as e:
        print("Error issuing the book:", e)
        session.rollback()
        raise RuntimeError("Ошибка при заполнения тестовыми данными")

    finally:
        session.close()
