# Form implementation generated from reading ui file 'c:\Users\grubg\Documents\KULIAH\Pemdes-W01\UAS\PEMESANAN_MAKANAN\src\ui\makanan.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 426)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.judul = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.judul.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.judul.setFont(font)
        self.judul.setObjectName("judul")
        self.verticalLayout_4.addWidget(self.judul)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.namamakanan = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.namamakanan.setMinimumSize(QtCore.QSize(0, 40))
        self.namamakanan.setObjectName("namamakanan")
        self.horizontalLayout_7.addWidget(self.namamakanan)
        self.harga = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.harga.setMinimumSize(QtCore.QSize(0, 40))
        self.harga.setObjectName("harga")
        self.horizontalLayout_7.addWidget(self.harga)
        self.filter = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.filter.setMinimumSize(QtCore.QSize(0, 40))
        self.filter.setObjectName("filter")
        self.horizontalLayout_7.addWidget(self.filter)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableView = QtWidgets.QTableView(parent=self.verticalLayoutWidget)
        self.tableView.setMinimumSize(QtCore.QSize(0, 40))
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.tableView)
        self.SHOW_RECORD = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.SHOW_RECORD.setMinimumSize(QtCore.QSize(0, 40))
        self.SHOW_RECORD.setObjectName("SHOW_RECORD")
        self.verticalLayout_5.addWidget(self.SHOW_RECORD)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.UPDATE = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.UPDATE.setMinimumSize(QtCore.QSize(0, 40))
        self.UPDATE.setObjectName("UPDATE")
        self.horizontalLayout_4.addWidget(self.UPDATE)
        self.CANCEL = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.CANCEL.setMinimumSize(QtCore.QSize(0, 40))
        self.CANCEL.setObjectName("CANCEL")
        self.horizontalLayout_4.addWidget(self.CANCEL)
        self.DELETE = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.DELETE.setMinimumSize(QtCore.QSize(0, 40))
        self.DELETE.setObjectName("DELETE")
        self.horizontalLayout_4.addWidget(self.DELETE)
        self.ADD = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.ADD.setMinimumSize(QtCore.QSize(0, 40))
        self.ADD.setObjectName("ADD")
        self.horizontalLayout_4.addWidget(self.ADD)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.judul.setText(_translate("Form", "MAKANAN"))
        self.namamakanan.setPlaceholderText(_translate("Form", "NAMA MAKANAN"))
        self.harga.setPlaceholderText(_translate("Form", "HARGA"))
        self.filter.setText(_translate("Form", "FILTER"))
        self.SHOW_RECORD.setText(_translate("Form", "SHOW RECORD"))
        self.UPDATE.setText(_translate("Form", "UPDATE"))
        self.CANCEL.setText(_translate("Form", "CANCEL"))
        self.DELETE.setText(_translate("Form", "DELETE"))
        self.ADD.setText(_translate("Form", "ADD"))