from PyQt6.QtWidgets import QDialog
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from datetime import datetime
from src.ui.kasirrecord_ui import Ui_Dialog
from src.errorDialog import ErrorDialog
import os


class KasirRecord(Ui_Dialog, QDialog):
    def __init__(self, recordNo, db):
        super().__init__()
        self.setupUi(self)
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
        # self.UPDATE.clicked.connect(self.update)
        

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


    # def update(self):
    #     record = self.model.record(self.recordNo)
    #     query = QSqlQuery()
    #     currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     query_id_pembeli = f"SELECT id_pembeli FROM pembeli WHERE nama_pembeli = '{record.value("nama_pembeli")}'"
    #     query_id_makanan = f"SELECT id_makanan FROM makanan WHERE nama_makanan = '{record.value("nama_makanan")}'"
    #     query_id_kasir = f"SELECT id_kasir FROM kasir WHERE nama_kasir = '{record.value("nama_kasir")}'"
    #     id_pembeli = self.fetchOneQuery(query_id_pembeli, query)
    #     id_makanan = self.fetchOneQuery(query_id_makanan, query)
    #     id_kasir = self.fetchOneQuery(query_id_kasir, query)
    #     if not len(record.value("nama_makanan")) or not len(record.value("nama_pembeli")) or not len(record.value("nama_kasir")) or not record.value("jumlah"):
    #         errorDialog = ErrorDialog("Data Tidak Valid")
    #         errorDialog.exec()
    #         return
    #     else:
    #         if id_pembeli == None:
    #             errorDialog = ErrorDialog("nama pembeli tidak ada dalam daftar, lihat tab pembeli untuk melihat daftar pembeli")
    #             errorDialog.exec()
    #             return
    #         elif id_makanan == None:
    #             errorDialog = ErrorDialog("makanan tidak ada dalam daftar, lihat tab makanan untuk melihat daftar makanan")
    #             errorDialog.exec()
    #             return
    #         elif id_kasir == None:
    #             errorDialog = ErrorDialog("nama kasir tidak ada dalam daftar, lihat tab kasir untuk melihat daftar kasir")
    #             errorDialog.exec()
    #             return
            
    #     jumlah = int(record.value("jumlah"))
    #     discount = int(record.value("discount"))
    #     harga_makanan = int(self.fetchOneQuery(f"SELECT harga FROM makanan WHERE nama_makanan = '{record.value("nama_makanan")}'", query))
    #     total_harga = harga_makanan * jumlah - ((harga_makanan * jumlah) * (int(discount)/100))
    #     id_transaksi = record.value("id_transaksi")
    #     query.exec(f"""
    #         UPDATE transaksi 
    #         SET id_pembeli = '{id_pembeli}', id_makanan = '{id_makanan}', id_kasir = '{id_kasir}', jumlah = '{jumlah}', tanggal_transaksi = '{currentTime}', total_harga = '{total_harga}', discount = '{discount}'
    #         WHERE id_transaksi = '{self.recordNo}'
    #     """)
    #     # self.refresh()
    #     self.displayRecord()      
    #     # self.displayTable()
    
    
    
    # def fetchOneQuery(self, query_str, query):
    #     query.exec(query_str)
    #     query.next()
    #     return query.value(0)
    
    # def refresh(self):
    #     self.model = QSqlQueryModel()
    #     self.model.setQuery(f"SELECT t.id_transaksi, m.nama_makanan, t.jumlah ,m.harga, p.nama_pembeli, k.nama_kasir, t.total_harga, t.discount FROM transaksi AS t, pembeli AS p, kasir AS k, makanan AS m WHERE t.id_pembeli = p.id_pembeli AND t.id_makanan = m.id_makanan AND t.id_kasir = k.id_kasir")
