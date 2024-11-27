from PyQt6.QtWidgets import QDialog
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
from src.ui.pembelirecord_ui import Ui_Dialog
from src.errorDialog import ErrorDialog
import os






class PembeliRecord(Ui_Dialog, QDialog):
    def __init__(self, recordNo, db, parent):
        super().__init__()
        self.setupUi(self)
        self.recordNo = recordNo
        self.setWindowTitle("Pembeli Records")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.db = db
        self.parent = parent
        self.db.open()
        self.model = QSqlQueryModel()
        self.displayRecord()
        self.setFixedSize(self.size())

        self.previous.clicked.connect(self.prevRecord)
        self.next.clicked.connect(self.nextRecord)
        self.first.clicked.connect(self.firstRecord)
        self.last.clicked.connect(self.lastRecord)
        self.UPDATE.clicked.connect(self.update)
    


    def displayRecord(self):
        self.model.setQuery("SELECT * FROM pembeli")
        self.record = self.model.record(self.recordNo)
        self.IDPEMBELI.setText(str(self.record.value("id_pembeli")))
        self.nama.setText(str(self.record.value("nama_pembeli")))
        self.nomortlp.setText(str(self.record.value("no_telepon")))
    
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

        if len(self.nama.text()) < 1 or len(self.nomortlp.text()) < 1:
            errorDialog = ErrorDialog("Masukan Semua Data Yang di butuhkan")
            errorDialog.exec()
            return

        nama_pembeli = self.nama.text()
        no_telepon = self.nomortlp.text()
        print(nama_pembeli)
        query.exec(f"""
                UPDATE pembeli
                SET nama_pembeli = '{nama_pembeli}', no_telepon = '{no_telepon}'
                WHERE id_pembeli = {int(self.IDPEMBELI.text())}
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


  