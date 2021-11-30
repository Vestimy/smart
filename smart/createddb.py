from PySide6.QtSql import QSqlDatabase
from config import Config

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

    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName('new_test')
    db.setUserName('root')
