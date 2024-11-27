from PyQt6.QtWidgets import QWidget, QHeaderView
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from src.ui.makanan_ui import Ui_Form
from src.readOnly import ReadOnlyDelegate
from src.makananRecord import MakananRecord
from src.errorDialog import ErrorDialog
import os


class Makanan(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)

        self.delegate = ReadOnlyDelegate()
        self.setLayout(self.verticalLayout_4)

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(os.path.dirname(__file__), "db/pemesananMakanan.sqlite"))
        self.db.open()


        self.model = QSqlTableModel(db = self.db)
        self.model.setTable("makanan")

        self.tableView.setModel(self.model)

        self.model.select()
        self.UPDATE.clicked.connect(self.updateButton)
        self.filter.clicked.connect(self.updateFilter)
        self.CANCEL.clicked.connect(self.cancel)
        self.ADD.clicked.connect(self.addData)
        self.DELETE.clicked.connect(self.delete)
        self.SHOW_RECORD.clicked.connect(self.showRecord)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)



    def updateFilter(self):
        if len(self.namamakanan.text()) < 1 and len(self.harga.text()) < 1:
            self.model.setFilter("")
            return

        if len(self.namamakanan.text()) < 1:
            self.model.setFilter(f"harga <= {self.harga.text()}")
            return
        elif len(self.harga.text()) < 1: 
            self.model.setFilter(f"nama_makanan LIKE '%{self.namamakanan.text()}%'")
            return
        
        self.model.setFilter(f"nama_makanan LIKE '%{self.namamakanan.text()}%' AND harga <= {self.harga.text()}")




    def displayTable(self):
        self.tableView.setModel(self.model)
        self.model.select()

    
    def refresh(self):
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("makanan")
    
    def showRecord(self):
        no = self.tableView.currentIndex().row()
        self.displayTable()
        if self.model.rowCount() - 1 < no or no == -1:
            transaksiRecord = MakananRecord(0, self.db, self)
        else:
            transaksiRecord = MakananRecord(no, self.db, self)
        
        transaksiRecord.exec()  
    
    def readOnly(self):
        self.tableView.setItemDelegateForColumn(0, self.delegate)
    
    def addData(self):
        self.model.insertRow(self.model.rowCount())
        self.readOnly()
    
    def updateButton(self):
        record = self.model.record(self.tableView.currentIndex().row())
        query = QSqlQuery()

        if len(record.value("nama_makanan")) < 1 or record.value("harga") < 1:
            errorDialog = ErrorDialog("Masukan Semua Data Yang di butuhkan")
            errorDialog.exec()
            return

        nama_makanan = record.value("nama_makanan")
        harga = record.value("harga")

        if not record.value("id_makanan"):
            query.exec(f"""
                INSERT INTO makanan(nama_makanan, harga) VALUES('{nama_makanan}', '{harga}')
            """)
        else:
            id_makanan = record.value("id_makanan")

            # exist = self.fetchOneQuery(f"SELECT * FROM transaksi WHERE id_pembeli = '{id_kasir}'", query)
            # if exist != None:
            #     errorDialog = ErrorDialog("tidak bisa mengedit data, Data ini di gunakan di table transaksi")
            #     errorDialog.exec()
            #     return

            query.exec(f"""
                UPDATE makanan
                SET nama_makanan = '{nama_makanan}', harga = '{harga}'
                WHERE id_makanan = '{id_makanan}'
            """)
            self.refresh()
        self.displayTable()
    
    def delete(self):
        if self.tableView.currentIndex().row() == -1:
            return
        
        query = QSqlQuery()
        id_makanan = self.model.record(self.tableView.currentIndex().row()).value("id_makanan")
        exist = self.fetchOneQuery(f"SELECT * FROM transaksi WHERE id_makanan = '{id_makanan}'", query)
        print(exist)
        if exist != None:
            errorDialog = ErrorDialog("tidak bisa menghapus data, Data ini di gunakan di table transaksi")
            errorDialog.exec()
            return

        query.exec(f"DELETE FROM makanan WHERE id_makanan = '{id_makanan}'")
        self.displayTable()
    
    def cancel(self):
        self.model.revertAll()
    
     
    def fetchOneQuery(self, query_str, query):
        query.exec(query_str)
        query.next()
        return query.value(0)