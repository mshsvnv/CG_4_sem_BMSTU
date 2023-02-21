from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

class Canvas(QtWidgets.QWidget):
    
    def __init__(self, parent, addRow, curCoordLabel, pointsAll, actions, solution):
        super().__init__(parent)

        self.setMouseTracking(True)

        self.clean = False
        self.lastIndex = 0

        self.penFirst = QtGui.QPen(Qt.red, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.penSecond = QtGui.QPen(Qt.green, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

        self.painter = QtGui.QPainter()

        self.addRow = addRow
        self.curCoordLabel = curCoordLabel

        self.resPointsFirst = list()  
        self.resPointsSecond = list() 

        self.pointsAll = pointsAll    # информация о всех точках
        self.actions = actions

        self.maxValue = 10.0
        self.scale = 2 * self.maxValue / min(self.width(), self.height())

        self.solution = solution

    def toCanvas(self, point: list): # из фактических в канвас
        
        xValue = int(self.width() // 2 + point[0] / self.scale)
        yValue = int(self.height() // 2 - point[1] / self.scale)

        return [xValue, yValue]
    
    def fromCanvas(self, point: list): # из канваса в фактические

        xValue = (point[0] - self.width() // 2) * self.scale
        yValue = (-point[1] + self.height() // 2) * self.scale

        return [xValue, yValue]
    
    def prepareCanvas(self):

        self.painter.fillRect(0, 0, self.width(), self.height(), Qt.white)

        pen = QtGui.QPen(Qt.black, 1)

        axis = self.fromCanvas([self.width(), self.height()])

        self.painter.setPen(pen)
        self.painter.drawLine(QtCore.QPoint(self.width()//2, 0), QtCore.QPoint(self.width()//2, self.height()))
        self.painter.drawLine(QtCore.QPoint(0, self.height()//2), QtCore.QPoint(self.width(), self.height()//2))
        
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, self.height() // 2 - 5), "(0.0, 0.0)")
        self.painter.drawText(QtCore.QPoint(self.width() - 85, self.height() // 2 - 5), "({:.1f}, 0.0)".format(axis[0]))
        self.painter.drawText(QtCore.QPoint(0, self.height() // 2 - 5), "(-{:.1f}, 0.0)".format(axis[0]))
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, 20), "(0.0, {:.1f})".format(axis[1]))
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, self.height()), "(0.0, {:.1f})".format(axis[1]))

    def paintEvent(self, event):

        self.painter.begin(self)

        self.scale = 2 * self.maxValue / min(self.width(), self.height())

        self.prepareCanvas()
        
        i = 1

        for point in self.pointsAll:
            if point[2] == 1:
                self.painter.setPen(self.penFirst)
            else:
                self.painter.setPen(self.penSecond)

            xValue, yValue = self.toCanvas(point)

            drawPoint = QtCore.QPoint(xValue, yValue)

            self.painter.drawPoint(drawPoint)

            if self.width() - xValue < 80:
                xValue -= 100

            if yValue < 20:
                yValue += 20
            
            drawPoint = QtCore.QPoint(xValue, yValue)

            self.painter.drawText(drawPoint, " {}.({:.1f}, {:.1f})".format(i, point[0], point[1]))
            
            i += 1

        self.painter.end()

    def mouseMoveEvent(self, event):

        curCoord = self.fromCanvas([event.pos().x(), event.pos().y()])

        self.curCoordLabel.setText("({:.1f}, {:.1f})".format(curCoord[0], curCoord[1]))
        
    def mousePressEvent(self, event):

        setNum = 0

        if event.type() == QtCore.QEvent.MouseButtonPress:

            point = event.pos()

            if event.button() == QtCore.Qt.LeftButton:
                setNum = 1
            else:
                setNum = 2

            xValue, yValue = self.fromCanvas([point.x(), point.y()])

            self.addRow(xValue, yValue, setNum) 
            self.actions.append([xValue, yValue, setNum, "add"])
            self.pointsAll.append([xValue, yValue, setNum])
            
        self.update()
