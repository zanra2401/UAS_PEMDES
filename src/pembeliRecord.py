from PyQt6.QtWidgets import QDialog
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from src.ui.pembelirecord_ui import Ui_Dialog
from src.errorDialog import ErrorDialog
import os






class PembeliRecord(Ui_Dialog, QDialog):
    def __init__(self, recordNo):
        super().__init__()
        self.setupUi(self)
        self.recordNo = recordNo
        self.setWindowTitle("Pembeli Records")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(os.path.dirname(__file__), "db/pemesananMakanan.sqlite"))
        self.db.open()
        self.model = QSqlTableModel(db = self.db)
        self.model.setTable("pembeli")
        self.model.select()
        self.displayRecord()
        self.setFixedSize(self.size())

        self.previous.clicked.connect(self.prevRecord)
        self.next.clicked.connect(self.nextRecord)
        self.first.clicked.connect(self.firstRecord)
        self.last.clicked.connect(self.lastRecord)
    


    def displayRecord(self):
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

  