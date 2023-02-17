# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mshsvnv/Рабочий стол/CG_4_sem_BMSTU/lab_01/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1410, 1038)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.setAddLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setAddLabel.setFont(font)
        self.setAddLabel.setObjectName("setAddLabel")
        self.gridLayout.addWidget(self.setAddLabel, 2, 1, 1, 1)
        self.xAddLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.xAddLineEdit.setObjectName("xAddLineEdit")
        self.gridLayout.addWidget(self.xAddLineEdit, 0, 2, 1, 1)
        self.cleanButton = QtWidgets.QPushButton(self.centralwidget)
        self.cleanButton.setObjectName("cleanButton")
        self.gridLayout.addWidget(self.cleanButton, 5, 1, 1, 3)
        self.cancleButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancleButton.setObjectName("cancleButton")
        self.gridLayout.addWidget(self.cancleButton, 3, 5, 1, 4)
        self.xAddLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.xAddLabel.setFont(font)
        self.xAddLabel.setObjectName("xAddLabel")
        self.gridLayout.addWidget(self.xAddLabel, 0, 1, 1, 1)
        self.pointNumLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pointNumLabel.setFont(font)
        self.pointNumLabel.setObjectName("pointNumLabel")
        self.gridLayout.addWidget(self.pointNumLabel, 0, 5, 1, 1)
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton.setStyleSheet("color = rgb(143, 100, 164)")
        self.solveButton.setObjectName("solveButton")
        self.gridLayout.addWidget(self.solveButton, 5, 5, 1, 4)
        self.yAddLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yAddLineEdit.setObjectName("yAddLineEdit")
        self.gridLayout.addWidget(self.yAddLineEdit, 1, 2, 1, 1)
        self.setAddLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.setAddLineEdit.setObjectName("setAddLineEdit")
        self.gridLayout.addWidget(self.setAddLineEdit, 2, 2, 1, 1)
        self.yAddLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yAddLabel.setFont(font)
        self.yAddLabel.setObjectName("yAddLabel")
        self.gridLayout.addWidget(self.yAddLabel, 1, 1, 1, 1)
        self.pointDelLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pointDelLineEdit.setObjectName("pointDelLineEdit")
        self.gridLayout.addWidget(self.pointDelLineEdit, 0, 7, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setEnabled(True)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 3, 1, 1, 3)
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setEnabled(True)
        self.delButton.setObjectName("delButton")
        self.gridLayout.addWidget(self.delButton, 1, 5, 1, 3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 4, 7, 1, 1, QtCore.Qt.AlignRight)
        self.labelCanvas = QtWidgets.QLabel(self.centralwidget)
        self.labelCanvas.setAutoFillBackground(True)
        self.labelCanvas.setStyleSheet("bg: rgb(255, 255, 255)")
        self.labelCanvas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelCanvas.setObjectName("labelCanvas")
        self.gridLayout.addWidget(self.labelCanvas, 4, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1410, 25))
        self.menubar.setObjectName("menubar")
        self.infoMenu = QtWidgets.QMenu(self.menubar)
        self.infoMenu.setObjectName("infoMenu")
        MainWindow.setMenuBar(self.menubar)
        self.progInfo = QtWidgets.QAction(MainWindow)
        self.progInfo.setObjectName("progInfo")
        self.authorInfo = QtWidgets.QAction(MainWindow)
        self.authorInfo.setObjectName("authorInfo")
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.exitAction.setShortcutVisibleInContextMenu(False)
        self.exitAction.setObjectName("exitAction")
        self.infoMenu.addAction(self.progInfo)
        self.infoMenu.addAction(self.authorInfo)
        self.infoMenu.addSeparator()
        self.infoMenu.addAction(self.exitAction)
        self.menubar.addAction(self.infoMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа №1"))
        self.setAddLabel.setText(_translate("MainWindow", "Множество:"))
        self.cleanButton.setText(_translate("MainWindow", "Очистить"))
        self.cleanButton.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.cancleButton.setText(_translate("MainWindow", "Отмена"))
        self.cancleButton.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.xAddLabel.setText(_translate("MainWindow", "X:"))
        self.pointNumLabel.setText(_translate("MainWindow", "№ точки:"))
        self.solveButton.setText(_translate("MainWindow", "Решить"))
        self.solveButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.yAddLabel.setText(_translate("MainWindow", "Y:"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.addButton.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))
        self.delButton.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.labelCanvas.setText(_translate("MainWindow", "TextLabel"))
        self.infoMenu.setTitle(_translate("MainWindow", "Справка"))
        self.progInfo.setText(_translate("MainWindow", "О программе"))
        self.authorInfo.setText(_translate("MainWindow", "Об авторе"))
        self.exitAction.setText(_translate("MainWindow", "Выход"))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+E"))
