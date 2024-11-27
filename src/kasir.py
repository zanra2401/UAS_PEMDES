from PyQt6.QtWidgets import QWidget, QHeaderView
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from src.ui.kasir_ui import Ui_Kasir
from src.kasirRecord import KasirRecord
from src.errorDialog import ErrorDialog
from src.readOnly import ReadOnlyDelegate
import os


class Kasir(Ui_Kasir, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.verticalLayout)
        self.delegate = ReadOnlyDelegate()

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(os.path.dirname(__file__), "db/pemesananMakanan.sqlite"))
        self.db.open()

        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("kasir")

        self.readOnly()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)

        self.tableView.setModel(self.model)
        self.model.select()

        self.UPDATE.clicked.connect(self.updateButton)
        self.DELETE.clicked.connect(self.delete)
        self.CANCEL.clicked.connect(self.cancel)
        self.ADD.clicked.connect(self.addData)
        self.SHOW_RECORD.clicked.connect(self.showRecord)
        self.filter.clicked.connect(self.updateFilter)
    
    def updateFilter(self):
        if len(self.namakasir.text()) < 1 and len(self.idkasir.text()) < 1:
            self.model.setFilter("")
            return

        if len(self.namakasir.text()) < 1:
            self.model.setFilter(f"id_kasir LIKE '%{self.idkasir.text()}%'")
            return
        elif len(self.idkasir.text()) < 1:
            self.model.setFilter(f"nama_kasir LIKE '%{self.namakasir.text()}%'")
            return
        
        self.model.setFilter(f"nama_kasir LIKE '%{self.namakasir.text()}%' AND id_kasir LIKE '%{self.idkasir.text()}%'")




    def displayTable(self):
        self.tableView.setModel(self.model)
        self.model.select()

    
    def refresh(self):
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("kasir")
    
    def showRecord(self):
        no = self.tableView.currentIndex().row()
        self.displayTable()
        if self.model.rowCount() - 1 < no or no == -1:
            transaksiRecord = KasirRecord(0, self.db, self)
        else:
            transaksiRecord = KasirRecord(no, self.db, self)
        
        transaksiRecord.exec()  
    
    def readOnly(self):
        self.tableView.setItemDelegateForColumn(0, self.delegate)
    
    def addData(self):
        self.model.insertRow(self.model.rowCount())
        self.readOnly()
    
    def updateButton(self):
        record = self.model.record(self.tableView.currentIndex().row())
        query = QSqlQuery()

        if len(record.value("nama_kasir")) < 1 or len(record.value("shift")) < 1:
            errorDialog = ErrorDialog("Masukan Semua Data Yang di butuhkan")
            errorDialog.exec()
            return

        nama_kasir = record.value("nama_kasir")
        shift = record.value("shift")

        if not record.value("id_kasir"):
            query.exec(f"""
                INSERT INTO kasir(nama_kasir, shift) VALUES('{nama_kasir}', '{shift}')
            """)
        else:
            id_kasir = record.value("id_kasir")

            # exist = self.fetchOneQuery(f"SELECT * FROM transaksi WHERE id_pembeli = '{id_kasir}'", query)
            # if exist != None:
            #     errorDialog = ErrorDialog("tidak bisa mengedit data, Data ini di gunakan di table transaksi")
            #     errorDialog.exec()
            #     return

            query.exec(f"""
                UPDATE kasir
                SET nama_kasir = '{nama_kasir}', shift = '{shift}'
                WHERE id_kasir = '{id_kasir}'
            """)
            self.refresh()
        self.displayTable()
    
    def delete(self):
        if self.tableView.currentIndex().row() == -1:
            return
        
        query = QSqlQuery()
        id_kasir = self.model.record(self.tableView.currentIndex().row()).value("id_kasir")
        exist = self.fetchOneQuery(f"SELECT * FROM transaksi WHERE id_pembeli = '{id_kasir}'", query)
        if exist != None:
            errorDialog = ErrorDialog("tidak bisa menghapus data, Data ini di gunakan di table transaksi")
            errorDialog.exec()
            return

        query.exec(f"DELETE FROM kasir WHERE id_kasir = '{id_kasir}'")
        self.displayTable()
    
    def cancel(self):
        self.model.revertAll()
    
     
    def fetchOneQuery(self, query_str, query):
        query.exec(query_str)
        query.next()
        return query.value(0)