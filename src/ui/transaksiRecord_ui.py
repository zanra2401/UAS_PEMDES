# Form implementation generated from reading ui file 'c:\Users\grubg\Documents\KULIAH\Pemdes-W01\UAS\PEMESANAN_MAKANAN\src\ui\transaksiRecord.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TransaksiRecord(object):
    def setupUi(self, TransaksiRecord):
        TransaksiRecord.setObjectName("TransaksiRecord")
        TransaksiRecord.resize(580, 651)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=TransaksiRecord)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 548, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.MainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.MainLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setObjectName("MainLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.MainLayout.addWidget(self.label)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.ID = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.ID.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ID.sizePolicy().hasHeightForWidth())
        self.ID.setSizePolicy(sizePolicy)
        self.ID.setObjectName("ID")
        self.verticalLayout_2.addWidget(self.ID)
        self.verticalLayout_14.addLayout(self.verticalLayout_2)
        self.MainLayout.addLayout(self.verticalLayout_14)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.Maknan = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.Maknan.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Maknan.sizePolicy().hasHeightForWidth())
        self.Maknan.setSizePolicy(sizePolicy)
        self.Maknan.setObjectName("Maknan")
        self.verticalLayout_13.addWidget(self.Maknan)
        self.MainLayout.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        self.Pembeli = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.Pembeli.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pembeli.sizePolicy().hasHeightForWidth())
        self.Pembeli.setSizePolicy(sizePolicy)
        self.Pembeli.setObjectName("Pembeli")
        self.verticalLayout_12.addWidget(self.Pembeli)
        self.MainLayout.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.Kasir = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Kasir.sizePolicy().hasHeightForWidth())
        self.Kasir.setSizePolicy(sizePolicy)
        self.Kasir.setObjectName("Kasir")
        self.verticalLayout_11.addWidget(self.Kasir)
        self.MainLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.Total = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.Total.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Total.sizePolicy().hasHeightForWidth())
        self.Total.setSizePolicy(sizePolicy)
        self.Total.setObjectName("Total")
        self.verticalLayout_8.addWidget(self.Total)
        self.MainLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.Tanggal = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.Tanggal.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tanggal.sizePolicy().hasHeightForWidth())
        self.Tanggal.setSizePolicy(sizePolicy)
        self.Tanggal.setObjectName("Tanggal")
        self.verticalLayout_10.addWidget(self.Tanggal)
        self.MainLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.Jumlah = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Jumlah.sizePolicy().hasHeightForWidth())
        self.Jumlah.setSizePolicy(sizePolicy)
        self.Jumlah.setObjectName("Jumlah")
        self.verticalLayout_9.addWidget(self.Jumlah)
        self.MainLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_16.addWidget(self.label_11)
        self.Discount = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Discount.sizePolicy().hasHeightForWidth())
        self.Discount.setSizePolicy(sizePolicy)
        self.Discount.setObjectName("Discount")
        self.verticalLayout_16.addWidget(self.Discount)
        self.MainLayout.addLayout(self.verticalLayout_16)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FIRST = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FIRST.sizePolicy().hasHeightForWidth())
        self.FIRST.setSizePolicy(sizePolicy)
        self.FIRST.setObjectName("FIRST")
        self.horizontalLayout_2.addWidget(self.FIRST)
        self.PREV = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PREV.sizePolicy().hasHeightForWidth())
        self.PREV.setSizePolicy(sizePolicy)
        self.PREV.setObjectName("PREV")
        self.horizontalLayout_2.addWidget(self.PREV)
        self.NEXT = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NEXT.sizePolicy().hasHeightForWidth())
        self.NEXT.setSizePolicy(sizePolicy)
        self.NEXT.setObjectName("NEXT")
        self.horizontalLayout_2.addWidget(self.NEXT)
        self.LAST = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LAST.sizePolicy().hasHeightForWidth())
        self.LAST.setSizePolicy(sizePolicy)
        self.LAST.setObjectName("LAST")
        self.horizontalLayout_2.addWidget(self.LAST)
        self.MainLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(TransaksiRecord)
        QtCore.QMetaObject.connectSlotsByName(TransaksiRecord)

    def retranslateUi(self, TransaksiRecord):
        _translate = QtCore.QCoreApplication.translate
        TransaksiRecord.setWindowTitle(_translate("TransaksiRecord", "Dialog"))
        self.label.setText(_translate("TransaksiRecord", "DATA TRANSAKSI RECORD"))
        self.label_2.setText(_translate("TransaksiRecord", "Transaksi ID:"))
        self.label_5.setText(_translate("TransaksiRecord", "Nama Makanan:"))
        self.label_6.setText(_translate("TransaksiRecord", "Nama Pembeli:"))
        self.label_7.setText(_translate("TransaksiRecord", "Nama Kasir:"))
        self.label_10.setText(_translate("TransaksiRecord", "Total Harga:"))
        self.label_8.setText(_translate("TransaksiRecord", "Tanggal Pembelian:"))
        self.label_9.setText(_translate("TransaksiRecord", "Jumlah Pembelian:"))
        self.label_11.setText(_translate("TransaksiRecord", "Discount:"))
        self.FIRST.setText(_translate("TransaksiRecord", "First"))
        self.PREV.setText(_translate("TransaksiRecord", "Previous"))
        self.NEXT.setText(_translate("TransaksiRecord", "Next"))
        self.LAST.setText(_translate("TransaksiRecord", "Last"))