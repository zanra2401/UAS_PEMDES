# Form implementation generated from reading ui file 'c:\Users\grubg\Documents\KULIAH\Pemdes-W01\UAS\PEMESANAN_MAKANAN\src\ui\kasirrecord.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(504, 390)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 385))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kasirrecord = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.kasirrecord.setFont(font)
        self.kasirrecord.setObjectName("kasirrecord")
        self.verticalLayout.addWidget(self.kasirrecord)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelidkasir = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.labelidkasir.setObjectName("labelidkasir")
        self.verticalLayout_4.addWidget(self.labelidkasir)
        self.idkasir = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.idkasir.setEnabled(False)
        self.idkasir.setMinimumSize(QtCore.QSize(0, 40))
        self.idkasir.setObjectName("idkasir")
        self.verticalLayout_4.addWidget(self.idkasir)
        self.labelnamakasir = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.labelnamakasir.setObjectName("labelnamakasir")
        self.verticalLayout_4.addWidget(self.labelnamakasir)
        self.namakasir = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.namakasir.setMinimumSize(QtCore.QSize(0, 40))
        self.namakasir.setObjectName("namakasir")
        self.verticalLayout_4.addWidget(self.namakasir)
        self.labelshift = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.labelshift.setObjectName("labelshift")
        self.verticalLayout_4.addWidget(self.labelshift)
        self.shift = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.shift.setMinimumSize(QtCore.QSize(0, 40))
        self.shift.setObjectName("shift")
        self.verticalLayout_4.addWidget(self.shift)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.UPDATE = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UPDATE.sizePolicy().hasHeightForWidth())
        self.UPDATE.setSizePolicy(sizePolicy)
        self.UPDATE.setMinimumSize(QtCore.QSize(0, 40))
        self.UPDATE.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.UPDATE.setObjectName("UPDATE")
        self.verticalLayout.addWidget(self.UPDATE)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FIRST = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.FIRST.setMinimumSize(QtCore.QSize(0, 40))
        self.FIRST.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.FIRST.setObjectName("FIRST")
        self.horizontalLayout.addWidget(self.FIRST)
        self.PREV = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.PREV.setMinimumSize(QtCore.QSize(0, 40))
        self.PREV.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.PREV.setObjectName("PREV")
        self.horizontalLayout.addWidget(self.PREV)
        self.NEXT = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.NEXT.setMinimumSize(QtCore.QSize(0, 40))
        self.NEXT.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.NEXT.setObjectName("NEXT")
        self.horizontalLayout.addWidget(self.NEXT)
        self.LAST = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.LAST.setMinimumSize(QtCore.QSize(0, 40))
        self.LAST.setStyleSheet("background: #22177A;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 4px;")
        self.LAST.setObjectName("LAST")
        self.horizontalLayout.addWidget(self.LAST)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.kasirrecord.setText(_translate("Dialog", "KASIR RECORD"))
        self.labelidkasir.setText(_translate("Dialog", "ID KASIR"))
        self.labelnamakasir.setText(_translate("Dialog", "NAMA KASIR"))
        self.labelshift.setText(_translate("Dialog", "SHIFT"))
        self.UPDATE.setText(_translate("Dialog", "UPDATE"))
        self.FIRST.setText(_translate("Dialog", "FIRST"))
        self.PREV.setText(_translate("Dialog", "PREVIOUS"))
        self.NEXT.setText(_translate("Dialog", "NEXT"))
        self.LAST.setText(_translate("Dialog", "LAST"))
