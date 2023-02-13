from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

import sys

class MainUI(QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("main.ui", self)

        # Таблица
        # self.tableWidget.setColumnWidth(0, )

        canvas = QtGui.QPixmap(self.canvasLabel.size())
        canvas.fill(Qt.white)
        self.canvasLabel.setPixmap(canvas)

        # Меню
        self.progInfo.triggered.connect(self.printProgInfo)
        self.authorInfo.triggered.connect(self.printAuthorInfo)
        self.exitAction.triggered.connect(self.exitProgram)

    def printProgInfo(self):
        msg = QMessageBox(QMainWindow)
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
        msg = QMessageBox(QMainWindow)
        msg.setWindowTitle("Об авторе")
        msg.setText("Савинова Мария ИУ7-31Б")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel)

        x = msg.exec_()

    def mouseMoveEvent(self, event):
        painter = QtGui.QPainter(self.canvasLabel.pixmap())
        painter.drawPoint(event.x(), event.y())
        print(event.x, event.y)
        painter.end()
        self.update()


    def exitProgram(self):
        sys.exit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
