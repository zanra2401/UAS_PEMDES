from src.transaksi import Transaksi
from PyQt6.QtWidgets import QMainWindow, QApplication, QTabWidget
from PyQt6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.transaksi_widget = transaksi_widget = Transaksi()

        self.setMinimumSize(self.transaksi_widget.size())
        self.setCentralWidget(self.tabContainer())
    
    def tabContainer(self):
        tab = QTabWidget(self)
        tab.addTab(self.transaksi_widget, "Transaksi")

        return tab





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

