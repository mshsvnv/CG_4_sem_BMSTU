from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QApplication, QTableWidgetItem
import sys

from graphicsView import GraphicsView
# from tableWidget import TableWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        font = QtGui.QFont()
        font.setPointSize(15)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1555, 1050)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = GraphicsView(self.centralwidget)
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView.setGeometry(QtCore.QRect(540, 30, 981, 961))
        # self.graphicsView.setMouseTracking(True)
        # self.graphicsView.setObjectName("graphicsView")

        self.ansLabel = QtWidgets.QLabel(self.centralwidget)
        self.ansLabel.setGeometry(QtCore.QRect(30, 670, 232, 28))
        self.ansLabel.setFont(font)
        self.ansLabel.setObjectName("ansLabel")

        self.ansLineEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ansLineEdit.setGeometry(QtCore.QRect(30, 710, 471, 281))
        self.ansLineEdit.setObjectName("ansLineEdit")

        self.coordsLabel = QtWidgets.QLabel(self.centralwidget)
        self.coordsLabel.setGeometry(QtCore.QRect(30, 50, 182, 23))
        self.coordsLabel.setFont(font)
        self.coordsLabel.setObjectName("coordsLabel")

        self.cleanButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.cleanAll())
        self.cleanButton.setGeometry(QtCore.QRect(420, 50, 84, 28))
        self.cleanButton.setObjectName("cleanButton")

        self.draw()
        # self.tableWidget = TableWidget(self.centralwidget)
        # self.tableWidget.setGeometry(QtCore.QRect(30, 90, 471, 192))

        self.cancleButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancleButton.setGeometry(QtCore.QRect(30, 300, 471, 28))
        self.cancleButton.setObjectName("cancleButton")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 430, 471, 132))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.xAddLabel = QtWidgets.QLabel(self.widget)
        self.xAddLabel.setFont(font)
        self.xAddLabel.setObjectName("xAddLabel")
        self.gridLayout.addWidget(self.xAddLabel, 0, 0, 1, 1)

        self.xAddLineEdit = QtWidgets.QLineEdit(self.widget)
        self.xAddLineEdit.setObjectName("xAddLineEdit")
        self.gridLayout.addWidget(self.xAddLineEdit, 0, 1, 1, 2)

        self.numDelLabel = QtWidgets.QLabel(self.widget)
        self.numDelLabel.setFont(font)
        self.numDelLabel.setObjectName("numDelLabel")
        self.gridLayout.addWidget(self.numDelLabel, 0, 3, 1, 1)

        self.numDelLineEdit = QtWidgets.QLineEdit(self.widget)
        self.numDelLineEdit.setObjectName("numDelLineEdit")
        self.gridLayout.addWidget(self.numDelLineEdit, 0, 4, 1, 2)

        self.yAddLabel = QtWidgets.QLabel(self.widget)
        self.yAddLabel.setFont(font)
        self.yAddLabel.setObjectName("yAddLabel")
        self.gridLayout.addWidget(self.yAddLabel, 1, 0, 1, 1)

        self.yAddLineEdit = QtWidgets.QLineEdit(self.widget)
        self.yAddLineEdit.setObjectName("yAddLineEdit")
        self.gridLayout.addWidget(self.yAddLineEdit, 1, 1, 1, 2)

        self.setAddLabel = QtWidgets.QLabel(self.widget)
        self.setAddLabel.setFont(font)
        self.setAddLabel.setObjectName("setAddLabel")
        self.gridLayout.addWidget(self.setAddLabel, 2, 0, 1, 2)

        self.setAddLineEdit = QtWidgets.QLineEdit(self.widget)
        self.setAddLineEdit.setObjectName("setAddLineEdit")
        self.gridLayout.addWidget(self.setAddLineEdit, 2, 2, 1, 1)

        self.addButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.addPoint())
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 3, 2, 1, 1)

        self.delButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.delPoint())
        self.delButton.setObjectName("delButton")
        self.gridLayout.addWidget(self.delButton, 1, 5, 1, 1)

        self.solveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.solveTask())
        self.solveButton.setGeometry(QtCore.QRect(420, 670, 80, 28))
        self.solveButton.setObjectName("solveButton")

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
        self.authorInfo.triggered.connect(self.printAuthorInfo)

        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.exitAction.setShortcutVisibleInContextMenu(True)
        self.exitAction.setObjectName("exitAction")
        self.exitAction.triggered.connect(self.exitProgram)

        self.infoMenu.addAction(self.progInfo)
        self.infoMenu.addAction(self.authorInfo)

        self.infoMenu.addSeparator()

        self.infoMenu.addAction(self.exitAction)
        self.menubar.addAction(self.infoMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @staticmethod
    def errorMsg(string):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(string)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel)

        x = msg.exec_()

    @staticmethod
    def infoMsg(string):
        msg = QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText(string)
        msg.setIcon(QMessageBox.Info)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    def addPoint(self):
        xValue = self.xAddLineEdit.text()
        yValue = self.xAddLineEdit.text()
        setNum = self.setAddLineEdit.text()

        try:
            xValue = float(xValue)
            yValue = float(yValue)
            setNum = int(setNum)
        except:
            Ui_MainWindow.errorMsg("Введены некорректные данные!")

            return
        
        if setNum != 1 and setNum != 2:
            Ui_MainWindow.errorMsg("Введен неверный номер множества!")

            return
        
        # TODO: если неверные координаты

        self.tableWidget.addRow(xValue, yValue, setNum)

    def delPoint(self):

        pointNum = self.numDelLineEdit.text()

        try:
            pointNum = int(pointNum)
        except:
            Ui_MainWindow.errorMsg("Введены некорректные данные!")

            return

        if not (0 <= pointNum <= self.tableWidget.rowCount() + 1):
            Ui_MainWindow.errorMsg("Введен неверный номер точки!")

            return

        self.tableWidget.delRow(pointNum)

    def cleanAll(self):

        curRow = self.tableWidget.rowCount()
        
        if (curRow == 0):
            Ui_MainWindow.infoMsg("Сначала введите точки!")
        else:
            # отчистить поле для рисования
            for i in range(curRow):
                self.tableWidget.delRow(curRow - i)
        

    def solveTask(self):
        self.ansLineEdit.setPlainText("Когда-нибудь здесь будет правильный ответ!")

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа №1"))
        self.ansLabel.setText(_translate("MainWindow", "Ответ:"))
        self.coordsLabel.setText(_translate("MainWindow", "Координаты точек:"))
        self.cleanButton.setText(_translate("MainWindow", "Очистить"))
        self.cleanButton.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.cancleButton.setText(_translate("MainWindow", "Отменить последне действие"))
        self.cancleButton.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.xAddLabel.setText(_translate("MainWindow", "X:"))
        self.numDelLabel.setText(_translate("MainWindow", "№ точки:"))
        self.yAddLabel.setText(_translate("MainWindow", "Y:"))
        self.setAddLabel.setText(_translate("MainWindow", "Множество:"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.addButton.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))
        self.delButton.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.solveButton.setText(_translate("MainWindow", "Решить"))
        self.solveButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.infoMenu.setTitle(_translate("MainWindow", "Справка"))
        self.progInfo.setText(_translate("MainWindow", "О программе"))
        self.authorInfo.setText(_translate("MainWindow", "Об авторе"))
        self.exitAction.setText(_translate("MainWindow", "Выход"))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+E"))

# class GraphicsView(QtWidgets.QGraphicsView):

#     def __init__(self, place):
#         super().__init__(place)

#         self.setGeometry(QtCore.QRect(540, 30, 981, 961))
#         self.setMouseTracking(True)

#         self.viewport().installEventFilter(self)

#     def eventFilter(self, source, event):
#         if event.type() == QtCore.QEvent.MouseButtonPress:
#             if event.button() == QtCore.Qt.LeftButton:
#                 print(event.x(), event.y())
#             else:
#                 print(event.x(), event.y())
#         return super(GraphicsView, self).eventFilter(source, event)
    
#     def drawAxis(self):
#         pass

#     def cleanScene(self):
#         pass

#     def drawSolve(self):
#         pass

# class TableWidget(QTableWidget):

#     def __init__(self, place):
#         super().__init__(0, 3, place)
#         self.setHorizontalHeaderLabels(["X", "Y", "Множество"])
#         # self.setRowCount(1)
#         self.setColumnCount(3)

#         self.setColumnWidth(0, 150)
#         self.setColumnWidth(1, 150)
#         self.setColumnWidth(2, 155)

#     def addRow(self, xValue, yValue, setNum):

#         curRow = self.currentRow() + 1
#         self.insertRow(curRow)

#         self.setItem(curRow, 0, QTableWidgetItem("{:.1f}".format(xValue)))
#         self.setItem(curRow, 1, QTableWidgetItem("{:.1f}".format(yValue)))
#         self.setItem(curRow, 2, QTableWidgetItem(str(setNum)))

#     def delRow(self, pointNum):

#         self.removeRow(pointNum - 1)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())