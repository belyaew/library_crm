from orm.database import get_session
from orm.entity import Worker, Auth, Position

session = get_session()


def get_lib_id_by_login(woker_login):
    worker_id = get_worker_id_by_login(woker_login)
    return session.query(Worker).filter_by(id=worker_id).first().lib_adress


def get_worker_id_by_login(woker_login):
    return session.query(Auth).filter_by(login=woker_login).first().worker_id


def get_position_by_login(woker_login):
    worker_id = get_worker_id_by_login(woker_login)
    pos_id = session.query(Worker).filter_by(id=worker_id).first().position
    return session.query(Position).filter_by(id=pos_id).first().position
