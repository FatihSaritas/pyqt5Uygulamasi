# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 564)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbl1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl1.setGeometry(QtCore.QRect(270, 10, 361, 192))
        self.tbl1.setAutoScroll(True)
        self.tbl1.setAlternatingRowColors(False)
        self.tbl1.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl1.setShowGrid(True)
        self.tbl1.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl1.setRowCount(30)
        self.tbl1.setColumnCount(3)
        self.tbl1.setObjectName("tbl1")
        self.tbl1.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl1.verticalHeader().setHighlightSections(True)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(260, 230, 113, 32))
        self.btn2.setObjectName("btn2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 45, 81))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setObjectName("label1")
        self.verticalLayout_2.addWidget(self.label1)
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setObjectName("label2")
        self.verticalLayout_2.addWidget(self.label2)
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setObjectName("label3")
        self.verticalLayout_2.addWidget(self.label3)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(90, 30, 137, 125))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ln1 = QtWidgets.QLineEdit(self.widget1)
        self.ln1.setObjectName("ln1")
        self.verticalLayout.addWidget(self.ln1)
        self.ln2 = QtWidgets.QLineEdit(self.widget1)
        self.ln2.setObjectName("ln2")
        self.verticalLayout.addWidget(self.ln2)
        self.cmb1 = QtWidgets.QComboBox(self.widget1)
        self.cmb1.setObjectName("cmb1")
        self.cmb1.addItem("")
        self.cmb1.setItemText(0, "")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.verticalLayout.addWidget(self.cmb1)
        self.btn1 = QtWidgets.QPushButton(self.widget1)
        self.btn1.setObjectName("btn1")
        self.verticalLayout.addWidget(self.btn1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(410, 230, 231, 32))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn3 = QtWidgets.QPushButton(self.widget2)
        self.btn3.setObjectName("btn3")
        self.horizontalLayout.addWidget(self.btn3)
        self.cmb2 = QtWidgets.QComboBox(self.widget2)
        self.cmb2.setObjectName("cmb2")
        self.cmb2.addItem("")
        self.cmb2.addItem("")
        self.horizontalLayout.addWidget(self.cmb2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kayıt Uygulaması"))
        self.tbl1.setSortingEnabled(False)
        self.btn2.setText(_translate("MainWindow", "Silme"))
        self.label1.setText(_translate("MainWindow", "Ad"))
        self.label2.setText(_translate("MainWindow", "Soy Ad"))
        self.label3.setText(_translate("MainWindow", "Şirket"))
        self.cmb1.setItemText(1, _translate("MainWindow", "Vestel"))
        self.cmb1.setItemText(2, _translate("MainWindow", "Apple"))
        self.btn1.setText(_translate("MainWindow", "Ekle"))
        self.btn3.setText(_translate("MainWindow", "Filtrele"))
        self.cmb2.setItemText(0, _translate("MainWindow", "Vestel"))
        self.cmb2.setItemText(1, _translate("MainWindow", "Apple"))
