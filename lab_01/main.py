from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import Qt
import sys

class UI(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        uic.loadUi("main.ui", self)

        self.pointsFirst = list()
        self.pointsSecond = list()

        self.canvas = Canvas(self.centralwidget, self.pointsFirst, self.pointsSecond, self.addRow, self.delRow)
        self.gridLayout.addWidget(self.canvas, 4, 0, 1, 4)

        self.addButton.clicked.connect(self.addRow)
        self.cancleButton.clicked.connect(self.cancleLastAct)
        
        self.styleTable()

        # TODO навесить функции на кнопки

        self.show()

    # функции для обработки таблицы
    def styleTable(self):

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Координаты", "Множество"])

        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 120)

    def addRow(self, xValue, yValue, setNum):

        curRow = self.tableWidget.rowCount()
        self.tableWidget.insertRow(curRow)

        self.tableWidget.setItem(curRow, 0, QtWidgets.QTableWidgetItem("{:.1f}, {:.1f}".format(xValue, yValue)))
        self.tableWidget.setItem(curRow, 1, QtWidgets.QTableWidgetItem(str(setNum)))

        self.canvas.update()
    
    def delRow(self, pointNum):

        self.tableWidget.removeRow(pointNum - 1)
        self.canvas.update()

    def cancleLastAct(self):
        # удалить последнюю точку с холста

        # удалить последнюю точку из таблицы
        pass


class Canvas(QtWidgets.QWidget):
    
    def __init__(self, parent, pointsFirst, pointsSecond, addRow, delRow):
        super().__init__(parent)

        self.setMouseTracking(True)

        self.penFirst = QtGui.QPen(Qt.red, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.penSecond = QtGui.QPen(Qt.green, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

        self.painter = QtGui.QPainter()

        self.addRow = addRow
        self.delRow = delRow

        self.resPointsFirst = list()  
        self.resPointsSecond = list() 

        self.pointsFirst = pointsFirst   # точки первого множества
        self.pointsSecond = pointsSecond # точки второго множества

        self.pointsAll = list() # список всех точек

    def paintEvent(self, event):

        self.painter.begin(self)

        # TODO: оси

        self.painter.fillRect(0, 0, self.width(), self.height(), Qt.white)

        self.painter.setPen(self.penFirst)
        for point in self.pointsFirst:
            self.painter.drawPoint(point)
            self.painter.drawText(point, "({}, {})".format(point.x(), point.y()))

        self.painter.setPen(self.penSecond)
        for point in self.pointsSecond:
            self.painter.drawPoint(point)
            self.painter.drawText(point, "({}, {})".format(point.x(), point.y()))

        self.painter.end()

    def mousePressEvent(self, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.pointsFirst.append(event.pos())
                self.addRow(event.pos().x(), event.pos().y(), 1)
            else:
                self.pointsSecond.append(event.pos())
                self.addRow(event.pos().x(), event.pos().y(), 2)

            self.pointsAll.append(event.pos())
            
        self.update()

    def clearCanvas(self):

        self.pixmap().fill(Qt.white)

        self.update()

    def undo(self):
        if len(self.pointsAll) == 0:
            # TODO: кинуть предупреждение
            pass
        else:
            if self.pointsAll[-1] in self.pointsFirst:
                self.pointsFirst.pop(-1)
            else:
                self.pointsSecond.pop(-1)
            
            self.pointsAll.pop(-1)
            self.delRow(len(self.pointsAll))

        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()
