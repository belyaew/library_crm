import sqlalchemy
from sqlalchemy import create_engine

from orm.database import engine
from orm.entity import Auth


def check_credentials(login, password):
    connection = engine.connect()
    result = connection.execute(sqlalchemy.select(True).where(Auth.login == login, Auth.password == password))
    return result.scalar() is not None