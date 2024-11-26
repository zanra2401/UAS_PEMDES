from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from src.ui.pembeli_ui import Ui_Form
from PyQt6.QtWidgets import QWidget, QHeaderView
from src.readOnly import ReadOnlyDelegate
from src.pembeliRecord import PembeliRecord
from src.errorDialog import ErrorDialog
import sys, os

class Pembeli(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.verticalLayout)
        self.delegate = ReadOnlyDelegate()

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(os.path.dirname(__file__), "db/pemesananMakanan.sqlite"))
        self.db.open()

        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.readOnly()
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("pembeli")
        self.displayTable()

        self.showrecord.clicked.connect(self.showRecord)
        self.DELETE.clicked.connect(self.delete)
        self.UPDATE.clicked.connect(self.updateButton)
        self.CANCEL.clicked.connect(self.cancel)
        self.ADD.clicked.connect(self.addData)
        self.filter.clicked.connect(self.updateFilter)
    

    def updateFilter(self):
        if len(self.namapembeli.text()) < 1 and len(self.nomortelepon.text()) < 1:
            self.model.setFilter("")
            return

        if len(self.namapembeli.text()) < 1:
            self.model.setFilter(f"no_telepon LIKE '%{self.nomortelepon.text()}%'")
            return
        elif len(self.nomortelepon.text()) < 1:
            self.model.setFilter(f"nama_pembeli LIKE '%{self.namapembeli.text()}%'")
            return
        
        self.model.setFilter(f"nama_pembeli LIKE '%{self.namapembeli.text()}%' AND '%{self.nomortelepon.text()}%'")




    def displayTable(self):
        self.tableView.setModel(self.model)
        self.model.select()

    
    def refresh(self):
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("pembeli")
    
    def showRecord(self):
        no = self.tableView.currentIndex().row()
        self.displayTable()
        if self.model.rowCount() - 1 < no or no == -1:
            transaksiRecord = PembeliRecord(0)
        else:
            transaksiRecord = PembeliRecord(self.tableView.currentIndex().row())
        
        transaksiRecord.exec()  
    
    def readOnly(self):
        self.tableView.setItemDelegateForColumn(0, self.delegate)
    
    def addData(self):
        self.model.insertRow(self.model.rowCount())
        self.readOnly()
    
    def updateButton(self):
        record = self.model.record(self.tableView.currentIndex().row())
        query = QSqlQuery()

        if len(record.value("nama_pembeli")) < 1 or len(record.value("no_telepon")) < 1:
            errorDialog = ErrorDialog("Masukan Semua Data Yang di butuhkan")
            errorDialog.exec()
            return

        nama_pembeli = record.value("nama_pembeli")
        no_telepon = record.value("no_telepon")

        if not record.value("id_pembeli"):
            query.exec(f"""
                INSERT INTO pembeli(nama_pembeli, no_telepon) VALUES('{nama_pembeli}', '{no_telepon}')
            """)
        else:
            id_pembeli = record.value("id_pembeli")

            exist = self.fetchOneQuery(f"SELECT * FROM transaksi WHERE id_pembeli = '{id_pembeli}'", query)


            # if exist != None:
            #     errorDialog = ErrorDialog("tidak bisa mengedit data, Data ini di gunakan di table transaksi")
            #     errorDialog.exec()
            #     return

            query.exec(f"""
                UPDATE PEMBELI
                SET nama_pembeli = '{nama_pembeli}', no_telepon = '{no_telepon}'
                WHERE id_pembeli = '{id_pembeli}'
            """)
            self.refresh()
        self.displayTable()
    
    def delete(self):
        if self.tableView.currentIndex().row() == -1:
            return
        
        query = QSqlQuery()
        id_pembeli = self.model.record(self.tableView.currentIndex().row()).value("id_pembeli")
        exist = self.fetchOneQuery(f"SELECT * FROM transaksi WHERE id_pembeli = '{id_pembeli}'", query)
        if exist != None:
            errorDialog = ErrorDialog("tidak bisa menghapus data, Data ini di gunakan di table transaksi")
            errorDialog.exec()
            return

        query.exec(f"DELETE FROM pembeli WHERE id_pembeli = '{id_pembeli}'")
        self.displayTable()
    
    def cancel(self):
        self.model.revertAll()
    
     
    def fetchOneQuery(self, query_str, query):
        query.exec(query_str)
        query.next()
        return query.value(0)