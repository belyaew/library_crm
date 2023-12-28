

from orm.database import get_session
from orm.entity import Reader

session = get_session()


def get_all_readers():
    return session.query(Reader).all()
