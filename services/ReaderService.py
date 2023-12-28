from sqlite3 import IntegrityError

from sqlalchemy import update

from orm.database import get_session
from orm.entity import Reader, Subscription, Worker, Position

session = get_session()


def get_all_readers():
    return session.query(Reader).all()


def get_all_subscriptions():
    return session.query(Subscription).all()


def handle_add_subscription(reader, subscription_type, expiration_date):
    try:
        sub = Subscription(reader_id=reader.id, subscription_type=subscription_type.currentData(),
                           expiration_date=expiration_date.toPyDate())
        session.add(sub)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise RuntimeError("Ошибка при оформлении подписки")
    finally:
        session.close()


def update_subscription(reader, subscription_type, expiration_date, sub):
    try:
        # Обновляем существующую запись в таблице Subscriptions
        stmt = update(Subscription).where(Subscription.id == sub.id)
        stmt = stmt.values(subscription_type=subscription_type.currentData(),
                           expiration_date=expiration_date.toPyDate())
        session.execute(stmt)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise RuntimeError("Ошибка при обновлении подписки")
    finally:
        session.close()


def get_all_workers():
    return session.query(Worker).all()

def get_all_positions():
    return session.query(Position).all()


def updete_position(worker, pos, window):
    try:
        stmt = (
            update(Worker)
            .where(Worker.id == worker.id)
            .values({'position': pos.id})
        )
        session.execute(stmt)
        session.commit()
        window.setText("Роль успешно обновлена")
    except IntegrityError:
        session.rollback()
        raise RuntimeError("Ошибка при обновлении должности")
    finally:
        session.close()