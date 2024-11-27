from PyQt6.QtWidgets import QDialog
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from datetime import datetime
from src.ui.makananRecord_ui import Ui_Dialog
from src.errorDialog import ErrorDialog
import os


class MakananRecord(Ui_Dialog, QDialog):
    def __init__(self, recordNo, db, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.recordNo = recordNo
        self.setWindowTitle("Makanan Record")
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
        self.model.setQuery("SELECT * FROM makanan")
        self.record = self.model.record(self.recordNo)
        self.ID.setText(str(self.record.value("id_makanan")))
        self.NAMA.setText(str(self.record.value("nama_makanan")))
        self.HARGA.setText(str(int(self.record.value("harga"))))
        
    
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
    
     
    def update(self):
        query = QSqlQuery(self.db)

        if len(self.NAMA.text()) < 1 or len(self.HARGA.text()) < 1:
            errorDialog = ErrorDialog("Masukan Semua Data Yang di butuhkan")
            errorDialog.exec()
            return

        nama_makanan = self.NAMA.text()
        harga = int(self.HARGA.text())
        query.exec(f"""
                UPDATE makanan
                SET nama_makanan = '{nama_makanan}', harga = '{harga}'
                WHERE id_makanan = {int(self.ID.text())}
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


  
  