from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

import numpy as np

class Canvas(QtWidgets.QWidget):

    def __init__(self, parent, xLineEdit, yLineEdit):

        super().__init__(parent)

        self.setMouseTracking(True)

        self.painter = QtGui.QPainter()

        self.strokes = 10
        self.maxValue = 3.0
        self.scale = 2 * self.maxValue / min(self.width(), self.height())

        self.minusHyperbola = None
        self.plusHyperbola = None
        self.parabola = None
        self.x = None
        self.x_1 = None
        self.x_2 = None

        self.mainPoint = None

        self.makeGraph()

        self.xLineEdit = xLineEdit
        self.yLineEdit = yLineEdit

    def movePoints(self, dx, dy):
        
        self.x_1 += dx
        self.plusHyperbola += dy

        self.x_2 += dx
        self.minusHyperbola += dy

        self.x += dx
        self.parabola += dy

    def scalePoints(self, x, y, kx, ky):

        self.mainPoint = [x, y]

        self.x_1 = x + (self.x_1 - x) * kx
        self.plusHyperbola = y + (self.plusHyperbola - y) * ky

        self.x_2 = x + (self.x_2 - x) * kx
        self.minusHyperbola = y + (self.minusHyperbola - y) * ky

        self.x = x + (self.x - x) * kx
        self.parabola = y + (self.parabola - y) * ky

    def rotatePoints(self, x, y, angle):

        self.mainPoint = [x, y]
        
        angle = np.radians(angle)

        cos = np.cos(angle)
        sin = np.sin(angle)

        for i in range(len(self.x_1)):
            x_old = self.x_1[i]
            self.x_1[i] = x + (self.x_1[i] - x) * cos + (y - self.plusHyperbola[i]) * sin
            self.plusHyperbola[i] = y + (x_old - x) * sin + (self.plusHyperbola[i] - y) * cos

        for i in range(len(self.x_2)):
            x_old = self.x_2[i]
            self.x_2[i] = x + (self.x_2[i] - x) * cos + (y - self.minusHyperbola[i]) * sin
            self.minusHyperbola[i] = y + (x_old - x) * sin + (self.minusHyperbola[i] - y) * cos

        for i in range(len(self.x)):
            x_old = self.x[i]
            self.x[i] = x + (self.x[i] - x) * cos + (y - self.parabola[i]) * sin
            self.parabola[i] = y + (x_old - x) * sin + (self.parabola[i] - y) * cos   

    def makeGraph(self):

        self.x_1 = np.linspace(-0.8, 0.1, 10)
        self.x_2 = np.linspace(-0.1, 0.8, 10)
        self.x = np.linspace(-0.8, 0.8, 20)

        self.plusHyperbola = np.exp(self.x_1)
        self.minusHyperbola = np.exp(self.x_1)[::-1]
        self.parabola = np.array([x ** 2 for x in self.x])

    def toCanvas(self, point: list): # из фактических в канвас
        
        xValue = int(self.width() // 2 + point[0] / self.scale)
        yValue = int(self.height() // 2 - point[1] / self.scale)

        return [xValue, yValue]
    
    def fromCanvas(self, point: list): # из канваса в фактические

        xValue = (point[0] - self.width() // 2) * self.scale
        yValue = (-point[1] + self.height() // 2) * self.scale

        return [xValue, yValue]

    def drawGraph(self):

        self.painter.setPen(QtGui.QPen(QtGui.QColor("#00008b"), 2))

        pointsAll = []
        
        points = []
        for i in range(len(self.plusHyperbola)):
            x, y = self.toCanvas([self.x_1[i], self.plusHyperbola[i]])

            point = QtCore.QPoint(x, y)
            points.append(point)
            
            if 0 < i < len(self.plusHyperbola) - 1:
                pointsAll.append(point)

        self.painter.drawPolyline(points)

        points = []
        for i in range(len(self.minusHyperbola)):
            x, y = self.toCanvas([self.x_2[i], self.minusHyperbola[i]])

            point = QtCore.QPoint(x, y)
            points.append(point)
            
            if 0 < i < len(self.minusHyperbola) - 1:
                pointsAll.append(point)

        self.painter.drawPolyline(points)

        points = []
        index = len(pointsAll)
        for i in range(len(self.parabola)):
            x, y = self.toCanvas([self.x[i], self.parabola[i]])

            point = QtCore.QPoint(x, y)
            points.append(point)

            if 1 < i < len(self.parabola) - 2:
                pointsAll.insert(index, point)

        # pointsAll.append(pointsAll[0])

        self.painter.drawPolyline(points)

        self.painter.setBrush(QtGui.QBrush(QtGui.QColor("#00008b"), Qt.VerPattern))
        self.painter.drawPolygon(pointsAll)
        
        if self.mainPoint is not None:

            self.painter.setPen(QtGui.QPen(Qt.red, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            x, y = self.toCanvas(self.mainPoint)

            self.painter.drawPoint(x, y)
            self.painter.drawText(QtCore.QPoint(x + 5, y + 5), "({:.1f}, {:.1f})".format(self.mainPoint[0],
                                                                                     self.mainPoint[1]))
        
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

                self.painter.drawText(QtCore.QPoint(self.width() // 2 - 20, yValue + 20), "Y")
                self.painter.drawText(QtCore.QPoint(xValue + 10, self.height() // 2 - 10), "{:.1f}".format(xAxis))
                self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, yValue + 20), "{:.1f}".format(yAxis))
            elif i == self.strokes:
                self.painter.drawText(QtCore.QPoint(xValue - 30, self.height() // 2 + 20), "X")
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
            self.mainPoint = self.fromCanvas([event.pos().x(), event.pos().y()])

        self.xLineEdit.setText("{:.1f}".format(self.mainPoint[0]))
        self.yLineEdit.setText("{:.1f}".format(self.mainPoint[1]))

        self.update()
