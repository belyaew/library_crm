from orm.database import get_session
from orm.entity import Worker, LibraryAddress, Auth

session = get_session()


def get_lib_name_by_login(woker_login):
    worker_id = session.query(Auth).filter_by(login=woker_login).first().worker_id
    lib_id = session.query(Worker).filter_by(id=worker_id).first().lib_adress
    return session.query(LibraryAddress).filter_by(id=lib_id).first().name

