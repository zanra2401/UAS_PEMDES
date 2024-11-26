from PyQt6.QtWidgets import QWidget, QStyledItemDelegate, QHeaderView
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation, QSqlQuery, QSqlRecord
from src.ui.transaksiUI import Ui_Form
from src.readOnly import ReadOnlyDelegate
from src.transaksiRecord import TransaksiRecord
from src.errorDialog import ErrorDialog
import os
from datetime import datetime




class Transaksi(Ui_Form, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(os.path.dirname(__file__), "db/pemesananMakanan.sqlite"))
        self.delegate = ReadOnlyDelegate()
        self.db.open()
        self.model = QSqlTableModel(db = self.db)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.verticalLayout)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.displayTable()
        
        # self.model.setTable("transaksi")
        # self.model.setRelation(self.model.fieldIndex("id_makanan"), QSqlRelation("makanan", "id_makanan", "nama_makanan"))
        # self.model.setRelation(self.model.fieldIndex("id_pembeli"), QSqlRelation("pembeli", "id_pembeli", "nama_pembeli"))
        # self.model.setRelation(self.model.fieldIndex("id_kasir"), QSqlRelation("kasir", "id_kasir", "nama_kasir"))
        # self.model.setRelation(self.model.fieldIndex("id_makanan"), QSqlRelation("makanan", "id_makanan", "harga"))
        # self.model.select()

        
        self.SHOW_RECORD.clicked.connect(self.showRecord)
        self.ADD.clicked.connect(self.addData)
        self.CANCEL.clicked.connect(self.cancel)
        self.FILTER.clicked.connect(self.update_filter)
        self.UPDATE.clicked.connect(self.update)
        self.DELETE.clicked.connect(self.delete)
    
    def displayTable(self):
        for row in range(self.model.rowCount()):
            if not self.model.index(row, 0).data():
                self.model.removeRow(row)
        self.model.setQuery("SELECT t.id_transaksi, m.nama_makanan, t.jumlah ,m.harga, p.nama_pembeli, k.nama_kasir, t.total_harga, t.discount FROM transaksi AS t, pembeli AS p, kasir AS k, makanan AS m WHERE t.id_pembeli = p.id_pembeli AND t.id_makanan = m.id_makanan AND t.id_kasir = k.id_kasir")
        self.tableView.setModel(self.model)
        self.tableView.reset()
        self.readOnlyCol()

    def refresh(self):
        self.model = QSqlTableModel(db = self.db)
    

    def readOnlyCol(self):
        self.tableView.setItemDelegateForColumn(0, self.delegate)
        self.tableView.setItemDelegateForColumn(3, self.delegate)
        self.tableView.setItemDelegateForColumn(6, self.delegate)

     
    def update_filter(self):
        if len(self.lineEdit.text()) < 1 and len(self.lineEdit_2.text()) < 1:
            self.model.setQuery("SELECT t.id_transaksi, m.nama_makanan, t.jumlah ,m.harga, p.nama_pembeli, k.nama_kasir, t.total_harga, t.discount FROM transaksi AS t, pembeli AS p, kasir AS k, makanan AS m WHERE t.id_pembeli = p.id_pembeli AND t.id_makanan = m.id_makanan AND t.id_kasir = k.id_kasir")
            return

        if len(self.lineEdit.text()) < 1:
            self.model.setQuery(f"SELECT t.id_transaksi, m.nama_makanan, t.jumlah, m.harga, p.nama_pembeli, k.nama_kasir, t.total_harga, t.discount FROM transaksi AS t, pembeli AS p, kasir AS k, makanan AS m WHERE t.id_pembeli = p.id_pembeli AND t.id_makanan = m.id_makanan AND t.id_kasir = k.id_kasir AND p.nama_pembeli LIKE '%{self.lineEdit_2.text()}%'")
        elif len(self.lineEdit_2.text()) < 1:
            self.model.setQuery(f"SELECT t.id_transaksi, m.nama_makanan, t.jumlah, m.harga, p.nama_pembeli, k.nama_kasir, t.total_harga, t.discount FROM transaksi AS t, pembeli AS p, kasir AS k, makanan AS m WHERE t.id_pembeli = p.id_pembeli AND t.id_makanan = m.id_makanan AND t.id_kasir = k.id_kasir AND m.nama_makanan LIKE '%{self.lineEdit.text()}%'")
        else:
            self.model.setQuery(f"SELECT t.id_transaksi, m.nama_makanan, t.jumlah, m.harga, p.nama_pembeli, k.nama_kasir, t.total_harga, t.discount FROM transaksi AS t, pembeli AS p, kasir AS k, makanan AS m WHERE t.id_pembeli = p.id_pembeli AND t.id_makanan = m.id_makanan AND t.id_kasir = k.id_kasir AND p.nama_pembeli LIKE '%{self.lineEdit_2.text()}%' AND m.nama_makanan LIKE '%{self.lineEdit.text()}%'")


    
    def showRecord(self):
        no = self.tableView.currentIndex().row()
        self.displayTable()
        if self.model.rowCount() - 1 < no or no == -1:
            transaksiRecord = TransaksiRecord(0, self.db)
        else:
            transaksiRecord = TransaksiRecord(no, self.db)
        
        transaksiRecord.exec()
    
    def addData(self):
        self.model.insertRow(self.model.rowCount())
        self.readOnlyCol()
    
    def cancel(self):
        self.model.revertAll()
    
    def update(self):
        record = self.model.record(self.tableView.currentIndex().row())
        query = QSqlQuery(self.db)
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query_id_pembeli = f"SELECT id_pembeli FROM pembeli WHERE nama_pembeli = '{record.value("nama_pembeli")}'"
        query_id_makanan = f"SELECT id_makanan FROM makanan WHERE nama_makanan = '{record.value("nama_makanan")}'"
        query_id_kasir = f"SELECT id_kasir FROM kasir WHERE nama_kasir = '{record.value("nama_kasir")}'"
        id_pembeli = self.fetchOneQuery(query_id_pembeli, query)
        id_makanan = self.fetchOneQuery(query_id_makanan, query)
        id_kasir = self.fetchOneQuery(query_id_kasir, query)
        if not len(record.value("nama_makanan")) or not len(record.value("nama_pembeli")) or not len(record.value("nama_kasir")) or not record.value("jumlah"):
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
            
        jumlah = int(record.value("jumlah"))
        discount = int(record.value("discount"))
        harga_makanan = int(self.fetchOneQuery(f"SELECT harga FROM makanan WHERE nama_makanan = '{record.value("nama_makanan")}'", query))
        total_harga = harga_makanan * jumlah - ((harga_makanan * jumlah) * (int(discount)/100))
        if not record.value("id_transaksi"):
            query.exec(f"""
                INSERT INTO transaksi(id_pembeli, id_makanan, id_kasir, jumlah, tanggal_transaksi, total_harga, discount)
                VALUES('{id_pembeli}', '{id_makanan}', '{id_kasir}', '{jumlah}', '{currentTime}', '{total_harga}', '{discount}')
            """)
        else:
            id_transaksi = record.value("id_transaksi")
            query.exec(f"""
                UPDATE transaksi 
                SET id_pembeli = '{id_pembeli}', id_makanan = '{id_makanan}', id_kasir = '{id_kasir}', jumlah = '{jumlah}', tanggal_transaksi = '{currentTime}', total_harga = '{total_harga}', discount = '{discount}'
                WHERE id_transaksi = '{id_transaksi}'
            """)
            self.refresh()
      
        self.displayTable()

    
    def fetchOneQuery(self, query_str, query):
        query.exec(query_str)
        query.next()
        return query.value(0)
        
    
    def delete(self):
        if self.tableView.currentIndex().row() < 0:
            return
        
        id_transaksi = self.model.record(self.tableView.currentIndex().row()).value("id_transaksi")
        query = QSqlQuery()
        query.exec(f"DELETE FROM transaksi WHERE id_transaksi = '{id_transaksi}'")
        self.displayTable()