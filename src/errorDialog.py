from PyQt6.QtWidgets import QDialog
from src.ui.ErrorDialog_ui import Ui_Error


class ErrorDialog(Ui_Error, QDialog):
    def __init__(self, errorMassage):
        super().__init__()
        self.setupUi(self)

        self.Error.setText(errorMassage)
        self.setWindowTitle("ERROR")