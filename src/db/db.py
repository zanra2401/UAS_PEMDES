from PyQt6.QtSql import QSqlDatabase
import os


db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName(os.path.join(os.path.dirname(__file__), "pemesananMakanan.sqlite"))
