from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from ui_add_window import Ui_addWindow
from ui_answer_window import Ui_answerWindow
from ui_delete_window import Ui_deleteWindow

import sys


class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        font = QtGui.QFont()
        font.setPointSize(15)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 716)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 31, 471, 601))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.coordsLabel = QtWidgets.QLabel(self.layoutWidget)
        
        self.coordsLabel.setFont(font)
        self.coordsLabel.setObjectName("coordsLabel")
        self.gridLayout_2.addWidget(self.coordsLabel, 0, 0, 1, 1)

        self.cleanButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cleanButton.setObjectName("cleanButton")
        self.gridLayout_2.addWidget(self.cleanButton, 0, 1, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 205)

        self.addButton = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.openAddWindow())
        self.addButton.setEnabled(True)
        self.addButton.setObjectName("addButton")
        self.gridLayout_2.addWidget(self.addButton, 2, 0, 1, 1)

        self.delButton = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.openDeleteWindow())
        self.delButton.setObjectName("delButton")
        self.gridLayout_2.addWidget(self.delButton, 2, 1, 1, 1)

        self.cancleButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancleButton.setObjectName("cancleButton")
        self.gridLayout_2.addWidget(self.cancleButton, 3, 0, 1, 1)

        self.answerButton = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.openAnswerWindow())
        self.answerButton.setObjectName("answerButton")
        self.gridLayout_2.addWidget(self.answerButton, 3, 1, 1, 1)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(540, 30, 731, 600))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName("graphicsView")

        MainWindow.setCentralWidget(self.centralwidget)

        # Меню

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 25))
        self.menubar.setObjectName("menubar")

        self.infoMenu = QtWidgets.QMenu(self.menubar)
        self.infoMenu.setObjectName("infoMenu")

        MainWindow.setMenuBar(self.menubar)
        self.progInfo = QtWidgets.QAction(MainWindow)
        self.progInfo.setObjectName("progInfo")
        self.progInfo.triggered.connect(self.printProgInfo)

        self.authorInfo = QtWidgets.QAction(MainWindow)
        self.authorInfo.setObjectName("authorInfo")
        self.progInfo.triggered.connect(self.printAuthorInfo)

        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.exitAction.setShortcutVisibleInContextMenu(True)
        self.exitAction.setObjectName("exitAction")

        self.infoMenu.addAction(self.progInfo)
        self.infoMenu.addAction(self.authorInfo)

        self.infoMenu.addSeparator()

        self.infoMenu.addAction(self.exitAction)
        self.menubar.addAction(self.infoMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def printProgInfo(self):
        msg = QMessageBox()
        msg.setWindowTitle("О программе")

        text = "На плоскости заданы 2 множества точек. " + \
            "Найти пару окружностей, каждая из которых проходит " + \
            "хотя бы через 3 различные точки одного и того же " + \
            "множества (окружности пары строятся на точках " + \
            "разных множеств) таких, что разность площадей " + \
            "четырехугольников, образованных центрами окружностей, " + \
            "точками внутренних общих касательных и точкой пересечения " + \
            "касательных, максимальна."

        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel)

        x = msg.exec_()
    
    def printAuthorInfo(self):
        msg = QMessageBox()
        msg.setWindowTitle("Об авторе")
        msg.setText("Савинова Мария ИУ7-31Б")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel)

        x = msg.exec_()

    def exitProgram(self):
        sys.exit()

    # Открытие побочных окон

    def openAddWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_addWindow()
        self.ui.setupUi(self.window)
        self.window.setFixedSize(self.window.size())
        self.window.show() 

    def openDeleteWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_deleteWindow()
        self.ui.setupUi(self.window)
        self.window.setFixedSize(self.window.size())
        self.window.show() 

    def openAnswerWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_answerWindow()
        self.ui.setupUi(self.window)
        self.window.setFixedSize(self.window.size())
        self.window.show() 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа №1"))
        self.coordsLabel.setText(_translate("MainWindow", "Координаты точек:"))
        self.cleanButton.setText(_translate("MainWindow", "Очистить"))
        self.cleanButton.setShortcut(_translate("MainWindow", "Ctrl+D"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "X"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Y"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Множество"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.addButton.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))
        self.delButton.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.cancleButton.setText(_translate("MainWindow", "Отмена"))
        self.cancleButton.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.answerButton.setText(_translate("MainWindow", "Решить"))
        self.answerButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.infoMenu.setTitle(_translate("MainWindow", "Справка"))
        self.progInfo.setText(_translate("MainWindow", "О программе"))
        self.authorInfo.setText(_translate("MainWindow", "Об авторе"))
        self.exitAction.setText(_translate("MainWindow", "Выход"))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+E"))
