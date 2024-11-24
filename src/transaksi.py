from PyQt6.QtWidgets import QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation
from src.ui.transaksiUI import Ui_Form
from src.transaksiRecord import TransaksiRecord
import os


class Transaksi(Ui_Form, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(os.path.dirname(__file__), "db/pemesananMakanan.sqlite"));
        self.db.open()

        self.setLayout(self.verticalLayout)

        self.model = QSqlRelationalTableModel(db = self.db)
        self.model.setTable("transaksi")
        self.model.setRelation(self.model.fieldIndex("id_pembeli"), QSqlRelation("pembeli", "id_pembeli", "nama_pembeli"))
        self.model.setRelation(self.model.fieldIndex("id_makanan"), QSqlRelation("makanan", "id_makanan", "nama_makanan"))
        self.model.setRelation(self.model.fieldIndex("id_kasir"), QSqlRelation("kasir", "id_kasir", "nama_kasir"))
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.hideColumn(self.model.fieldIndex("tanggal_transaksi"))
        self.SHOW_RECORD.clicked.connect(self.showRecord)

     
    def update_filter(self):
        if len(self.lineEdit.text()) < 1 and len(self.lineEdit_2.text()) < 1:
            return
        
        if len(self.lineEdit.text()) < 1:
            return
    
    def showRecord(self):
        if self.tableView.currentIndex().row() == -1:
            transaksiRecord = TransaksiRecord(0)
        else:
            transaksiRecord = TransaksiRecord(self.tableView.currentIndex().row())
        
        transaksiRecord.exec()







