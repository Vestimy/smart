from PySide6.QtSql import QSqlDatabase, QSqlQuery
from config import Config

Q = QSqlQuery()


def init_db():
    """
    init_db()
    Initializes the database.
    If tables "books" and "authors" are already in the database, do nothing.
    Return value: None or raises ValueError
    The error value is the QtSql error instance.
    """
    db_conf = Config()

    # def check(func, *args):
    #     if not func(*args):
    #         raise ValueError(func.__self__.lastError())

    qsqldatabase, hostname, databasename, username, password = db_conf.get_db()

    db = QSqlDatabase.addDatabase(qsqldatabase)
    db.setHostName(hostname)
    db.setDatabaseName(databasename)
    db.setUserName(username)
    return db


