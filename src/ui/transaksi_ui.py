# Form implementation generated from reading ui file 'c:\Users\grubg\Documents\KULIAH\Pemdes-W01\UAS\PEMESANAN_MAKANAN\src\ui\transaksi.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 648)
        Form.setStyleSheet("")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 821, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setStyleSheet("font-weight: bold;")
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setStyleSheet("font-weight: bold;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.FILTER = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.FILTER.setMinimumSize(QtCore.QSize(0, 40))
        self.FILTER.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.FILTER.setObjectName("FILTER")
        self.horizontalLayout_5.addWidget(self.FILTER)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tableView = QtWidgets.QTableView(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableView)
        self.SHOW_RECORD = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SHOW_RECORD.sizePolicy().hasHeightForWidth())
        self.SHOW_RECORD.setSizePolicy(sizePolicy)
        self.SHOW_RECORD.setMinimumSize(QtCore.QSize(0, 40))
        self.SHOW_RECORD.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.SHOW_RECORD.setObjectName("SHOW_RECORD")
        self.verticalLayout.addWidget(self.SHOW_RECORD)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.UPDATE = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.UPDATE.setMinimumSize(QtCore.QSize(0, 40))
        self.UPDATE.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.UPDATE.setObjectName("UPDATE")
        self.horizontalLayout_4.addWidget(self.UPDATE)
        self.CANCEL = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.CANCEL.setMinimumSize(QtCore.QSize(0, 40))
        self.CANCEL.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.CANCEL.setObjectName("CANCEL")
        self.horizontalLayout_4.addWidget(self.CANCEL)
        self.DELETE = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.DELETE.setMinimumSize(QtCore.QSize(0, 40))
        self.DELETE.setStyleSheet("background: #D91656;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.DELETE.setObjectName("DELETE")
        self.horizontalLayout_4.addWidget(self.DELETE)
        self.ADD = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.ADD.setMinimumSize(QtCore.QSize(0, 40))
        self.ADD.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.ADD.setObjectName("ADD")
        self.horizontalLayout_4.addWidget(self.ADD)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Transaksi"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "NAMA PELANGGAN"))
        self.lineEdit.setPlaceholderText(_translate("Form", "NAMA MAKANAN"))
        self.FILTER.setText(_translate("Form", "FILTER"))
        self.SHOW_RECORD.setText(_translate("Form", "SHOW RECORD"))
        self.UPDATE.setText(_translate("Form", "UPDATE"))
        self.CANCEL.setText(_translate("Form", "CANCEL"))
        self.DELETE.setText(_translate("Form", "DELETE"))
        self.ADD.setText(_translate("Form", "ADD"))
