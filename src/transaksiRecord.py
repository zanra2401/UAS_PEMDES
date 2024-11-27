from PyQt6.QtWidgets import QDialog
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from datetime import datetime
from src.ui.transaksiRecord_ui import Ui_TransaksiRecord
from src.errorDialog import ErrorDialog
import os


class TransaksiRecord(Ui_TransaksiRecord, QDialog):
    def __init__(self, recordNo, db, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.recordNo = recordNo
        self.setWindowTitle("Transaksi Records")
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
        self.model.setQuery(f"SELECT t.id_transaksi, m.nama_makanan, t.jumlah ,m.harga, p.nama_pembeli, k.nama_kasir, t.total_harga, t.discount FROM transaksi AS t, pembeli AS p, kasir AS k, makanan AS m WHERE t.id_pembeli = p.id_pembeli AND t.id_makanan = m.id_makanan AND t.id_kasir = k.id_kasir")
        self.record = self.model.record(self.recordNo)
        self.ID.setText(str(self.record.value("id_transaksi")))
        self.Makanan.setText(str(self.record.value("nama_makanan")))
        self.Pembeli.setText(str(self.record.value("nama_pembeli")))
        self.Kasir.setText(str(self.record.value("nama_kasir")))
        self.Jumlah.setText(str(self.record.value("jumlah")))
        self.Total.setText("Rp. " + str(int(self.record.value("total_harga"))))
        self.Discount.setText(str(self.record.value("discount")))
        self.Tanggal.setText(str(self.record.value("tanggal_transaksi")))
        
    
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
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query_id_pembeli = f"SELECT id_pembeli FROM pembeli WHERE nama_pembeli = '{self.Pembeli.text()}'"
        query_id_makanan = f"SELECT id_makanan FROM makanan WHERE nama_makanan = '{self.Makanan.text()}'"
        query_id_kasir = f"SELECT id_kasir FROM kasir WHERE nama_kasir = '{self.Kasir.text()}'"
        id_pembeli = self.fetchOneQuery(query_id_pembeli, query)
        id_makanan = self.fetchOneQuery(query_id_makanan, query)
        id_kasir = self.fetchOneQuery(query_id_kasir, query)
        if not len(self.Pembeli.text()) or not len(self.Pembeli.text()) or not len(self.Pembeli.text()) or not int(self.Jumlah.text()):
            errorDialog = ErrorDialog("Data Tidak Valid")
            errorDialog.exec()
            return
        else:
            if id_pembeli == None:
                errorDialog = ErrorDialog("nama pembeli tidak ada dalam daftar, lihat tab pembeli untuk melihat daftar pembeli")
                errorDialog.exec()
                return
            elif id_makanan == None:
                errorDialog = ErrorDialog("makanan tidak ada dalam daftar, lihat tab makanan untuk melihat daftar makanan")
                errorDialog.exec()
                return
            elif id_kasir == None:
                errorDialog = ErrorDialog("nama kasir tidak ada dalam daftar, lihat tab kasir untuk melihat daftar kasir")
                errorDialog.exec()
                return
            
        jumlah = int(self.Jumlah.text())
        discount = int(self.Discount.text())
        harga_makanan = int(self.fetchOneQuery(f"SELECT harga FROM makanan WHERE nama_makanan = '{self.Makanan.text()}'", query))
        total_harga = harga_makanan * jumlah - ((harga_makanan * jumlah) * (int(discount)/100))
        query.exec(f"""
            UPDATE transaksi 
            SET id_pembeli = '{id_pembeli}', id_makanan = '{id_makanan}', id_kasir = '{id_kasir}', jumlah = '{jumlah}', tanggal_transaksi = '{currentTime}', total_harga = '{total_harga}', discount = '{discount}'
            WHERE id_transaksi = {int(self.ID.text())}
        """)
        print(query.lastError().text())
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
