from PyQt6.QtWidgets import QDialog
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation
from src.ui.transaksiRecordUI import Ui_Dialog
import os


class TransaksiRecord(Ui_Dialog, QDialog):
    def __init__(self, recordNo):
        super().__init__()
        self.setupUi(self)
        self.recordNo = recordNo

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(os.path.dirname(__file__), "db/pemesananMakanan.sqlite"))
        self.db.open()
        self.model = QSqlRelationalTableModel(db = self.db)
        self.model.setTable("transaksi")
        self.model.setRelation(self.model.fieldIndex("id_pembeli"), QSqlRelation("pembeli", "id_pembeli", "nama_pembeli"))
        self.model.setRelation(self.model.fieldIndex("id_makanan"), QSqlRelation("makanan", "id_makanan", "nama_makanan"))
        self.model.setRelation(self.model.fieldIndex("id_kasir"), QSqlRelation("kasir", "id_kasir", "nama_kasir"))
        self.model.select()
        self.displayRecord()
        self.setFixedSize(self.size())
        

    def displayRecord(self):
        self.record = self.model.record(self.recordNo)
        print(self.record.field("id_transaksi").value())
        self.ID.setText(str(self.record.value("id_transaksi")))
        self.Maknan.setText(str(self.record.value("nama_makanan")))
        self.Pembeli.setText(str(self.record.value("nama_pembeli")))
        self.Kasir.setText(str(self.record.value("nama_kasir")))
        self.Jumlah.setText(str(self.record.value("jumlah")))
        self.Total.setText("Rp. " + str(int(self.record.value("total_harga"))))
        self.Discount.setText(str(self.record.value("discount")))
        self.Tanggal.setText(str(self.record.value("tanggal_transaksi")))