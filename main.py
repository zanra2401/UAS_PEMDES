from src.transaksi import Transaksi
from src.pembeli import Pembeli
from src.kasir import Kasir
from src.makanan import Makanan
from PyQt6.QtWidgets import QMainWindow, QApplication, QTabWidget, QPushButton
from PyQt6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.transaksi_widget = Transaksi()
        self.pembeli = Pembeli()
        self.kasir = Kasir()
        self.makanan = Makanan()

        self.setWindowTitle("Pemesanans Makanan")
        self.setMinimumSize(self.transaksi_widget.size())
        self.tab = self.tabContainer()
        self.setCentralWidget(self.tab)
        self.tab.currentChanged.connect(self.refreshTransaksi)

    
    def tabContainer(self):
        tab = QTabWidget(self)
        tab.addTab(self.transaksi_widget, "Transaksi")
        tab.addTab(self.pembeli, "Pembeli")
        tab.addTab(self.kasir, "Kasir")
        tab.addTab(self.makanan, "Makanan")
        
        return tab

    def refreshTransaksi(self):
        self.transaksi_widget.refresh()
        self.transaksi_widget.displayTable()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

