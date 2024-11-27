from PyQt6.QtWidgets import QDialog
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from datetime import datetime
from src.ui.kasirrecord_ui import Ui_Dialog
from src.errorDialog import ErrorDialog
import os


class KasirRecord(Ui_Dialog, QDialog):
    def __init__(self, recordNo, db, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.recordNo = recordNo
        self.setWindowTitle("Kasir Record")
        self.db = db
        self.db.open()
        self.model = QSqlQueryModel()
        self.displayRecord()
        self.setFixedSize(self.size())

        self.PREV.clicked.connect(self.prevRecord)
        self.NEXT.clicked.connect(self.nextRecord)
        self.FIRST.clicked.connect(self.firstRecord)
        self.LAST.clicked.connect(self.lastRecord)
        self.UPDATE.clicked.connect(self.update)
        

    def displayRecord(self):
        self.model.setQuery("SELECT * FROM kasir")
        self.record = self.model.record(self.recordNo)
        self.idkasir.setText(str(self.record.value("id_kasir")))
        self.namakasir.setText(str(self.record.value("nama_kasir")))
        self.shift.setText(str(self.record.value("shift")))
        
    
    def prevRecord(self):
        if self.recordNo < 1:
            return
        else:
            self.recordNo -= 1

        self.displayRecord()
    
    def nextRecord(self):
        if self.recordNo == self.model.rowCount() - 1:
            return
    
        self.recordNo += 1

        self.displayRecord()

    def firstRecord(self):
        self.recordNo = 0
        self.displayRecord()
    
    def lastRecord(self):
        self.recordNo = self.model.rowCount() - 1
        self.displayRecord()

    def update(self):
        query = QSqlQuery(self.db)

        if len(self.shift.text()) < 1 or len(self.namakasir.text()) < 1:
            errorDialog = ErrorDialog("Masukan Semua Data Yang di butuhkan")
            errorDialog.exec()
            return

        nama_kasir = self.namakasir.text()
        shift = self.shift.text()
        query.exec(f"""
                UPDATE kasir
                SET nama_kasir = '{nama_kasir}', shift = '{shift}'
                WHERE id_kasir = {int(self.idkasir.text())}
            """)

        self.refresh()
        self.parent.refresh()
        self.parent.displayTable()
        self.displayRecord()      
    
    
    
    def fetchOneQuery(self, query_str, query):
        query.exec(query_str)
        query.next()
        return query.value(0)
    
    def refresh(self):
        self.model = QSqlQueryModel()
        self.model.setQuery(f"SELECT t.id_transaksi, m.nama_makanan, t.jumlah ,m.harga, p.nama_pembeli, k.nama_kasir, t.total_harga, t.discount FROM transaksi AS t, pembeli AS p, kasir AS k, makanan AS m WHERE t.id_pembeli = p.id_pembeli AND t.id_makanan = m.id_makanan AND t.id_kasir = k.id_kasir")


  
  