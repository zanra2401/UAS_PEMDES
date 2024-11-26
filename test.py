from src.transaksi import Transaksi
from PyQt6.QtWidgets import QMainWindow, QApplication, QTabWidget, QPushButton
from PyQt6.QtCore import QSize
from src.ui.transaksiUI import Ui_Form
import sys

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
window = Test()
window.show()
app.exec()
