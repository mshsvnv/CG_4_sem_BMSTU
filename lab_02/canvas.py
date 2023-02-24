from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

import numpy as np

class Canvas(QtWidgets.QWidget):

    def __init__(self, parent):

        super().__init__(parent)

        self.setMouseTracking(True)

        self.painter = QtGui.QPainter()

        self.strokes = 10
        self.maxValue = 3.0
        self.scale = 2 * self.maxValue / min(self.width(), self.height())

        self.minusHyperbola = None
        self.plusHyperbola = None
        self.parabola = None

    def toCanvas(self, point: list): # из фактических в канвас
        
        xValue = int(self.width() // 2 + point[0] / self.scale)
        yValue = int(self.height() // 2 - point[1] / self.scale)

        return [xValue, yValue]
    
    def fromCanvas(self, point: list): # из канваса в фактические

        xValue = (point[0] - self.width() // 2) * self.scale
        yValue = (-point[1] + self.height() // 2) * self.scale

        return [xValue, yValue]

    def drawGraph(self):
        pass
        
    
    def drawGrid(self):

        for i in range(self.strokes):

            if i == self.strokes // 2:
                self.painter.setPen(QtGui.QPen(Qt.black, 2))
            else:
                self.painter.setPen(QtGui.QPen(QtGui.QColor("#d7d7d7"), Qt.DashLine, 1))
            
            xValue = int(self.width() * i / self.strokes)
            yValue = int(self.height() * i / self.strokes)

            self.painter.drawLine(QtCore.QPoint(xValue, 0),
                                  QtCore.QPoint(xValue, self.height()))
            
            self.painter.drawLine(QtCore.QPoint(0, yValue),
                                  QtCore.QPoint(self.width(), yValue))
            
    def drawStrokes(self):

        self.painter.setPen(QtGui.QPen(Qt.black, 2))
        
        for i in range(self.strokes):

            xValue = int(self.width() * i / self.strokes)
            yValue = int(self.height() * i / self.strokes)

            self.painter.drawLine(QtCore.QPoint(xValue, self.height() // 2 - 5),
                                  QtCore.QPoint(xValue, self.height() // 2 + 5))
            
            self.painter.drawLine(QtCore.QPoint(self.width() // 2 - 5, yValue),
                                  QtCore.QPoint(self.width() // 2 + 5, yValue))
              
    def drawCoords(self):

        self.painter.setPen(QtGui.QPen(Qt.black, 2))

        for i in range(self.strokes + 1):

            xValue = int(self.width() * i / self.strokes)
            yValue = int(self.height() * i / self.strokes)

            xAxis, yAxis = self.fromCanvas([xValue, yValue])

            if i == self.strokes // 2:
                self.painter.drawText(QtCore.QPoint(xValue + 10, self.height() // 2 - 10), "{:.1f}".format(xAxis))
            elif i == 0:
                self.painter.drawText(QtCore.QPoint(xValue + 10, self.height() // 2 - 10), "{:.1f}".format(xAxis))
                self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, yValue + 20), "{:.1f}".format(yAxis))
            elif i == self.strokes:
                self.painter.drawText(QtCore.QPoint(xValue - 30, self.height() // 2 - 10), "{:.1f}".format(xAxis))
                self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, yValue - 10), "{:.1f}".format(yAxis))
            else:
                self.painter.drawText(QtCore.QPoint(xValue - 10, self.height() // 2 - 10), "{:.1f}".format(xAxis))
                self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, yValue + 5), "{:.1f}".format(yAxis))

    def paintEvent(self, event: QtGui.QPaintEvent):

        self.painter.begin(self)

        self.scale = 2 * self.maxValue / min(self.width(), self.height())

        self.painter.setFont(QtGui.QFont('Ubuntu', 15))
        
        self.painter.fillRect(0, 0, self.width(), self.height(), Qt.white)

        self.drawGrid() # оси
        self.drawStrokes() # штрихи
        self.drawCoords()  # координаты

        self.drawGraph()

        self.painter.end()

    def mousePressEvent(self, event: QtGui.QMouseEvent):
       
        if event.type() == QtCore.QEvent.MouseButtonPress:
            print("hello")

    def movePoints(self):
        pass

    def rotatePoints(self):
        pass

    def scalePoints(self):
        pass
