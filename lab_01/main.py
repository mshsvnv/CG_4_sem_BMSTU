from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import Qt
import sys

import itertools as it
import calcAlg

class UI(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        uic.loadUi("main.ui", self)

        self.pointsAll = list()    # информация о всех точках
        self.actions = list()      # информация о всех действиях
        self.solution = list()     # решение

        self.canvas = Canvas(self.centralwidget, self.addRow, 
                             self.pointsAll, self.actions. self.solution)
        self.gridLayout.addWidget(self.canvas, 4, 0, 3, 4)

        self.addButton.clicked.connect(self.addCommand)
        self.delButton.clicked.connect(self.delCommand)
        self.cancelButton.clicked.connect(self.cancelCommand)
        self.changeButton.clicked.connect(self.changeCommand)
        self.solveButton.clicked.connect(self.solveCommand)

        self.exitAction.triggered.connect(self.exitProgram)
        self.progInfo.triggered.connect(self.printProgInfo)
        self.authorInfo.triggered.connect(self.printAuthorInfo)
        
        self.styleTable()

        self.show()

    def solveCommand(self):

        firstPoints = [point for point in self.pointsAll if point[-1] == 1]
        secondPoints = [point for point in self.pointsAll if point[-1] == 2]

        circlesFirst = list()
        circlesSecond = list()

        for points in it.combinations(firstPoints, 3):
            value = calcAlg.oneLine(points[0], points[1], points[2])

            if value:
                print("На одной")
            else:
                centerPoint = calcAlg.circleCenter(points[0], points[1], points[2])
                
                radius = calcAlg.lenBetwPoints(points[0], centerPoint)

                print("Не на одной")
            
            self.canvas.update()

    def cancelCommand(self):
    
        if len(self.actions) == 0:
            msg = MessageBox("Инфо",
                             "Не было выполнено ни одно действие!", 
                             QtWidgets.QMessageBox.Information)
            msg.show()

            return
        else:
            
            if self.actions[-1][-1] == "add":

                self.pointsAll.pop(-1)
                self.delRow(self.tableWidget.rowCount())
                
            elif self.actions[-1][-1] == "del":
                
                self.pointsAll.insert(self.actions[-1][2] - 1,
                                       self.actions[-1][:3])
                self.addRow(self.actions[-1][0], 
                            self.actions[-1][1],
                            self.actions[-1][2], 
                            self.actions[-1][3] - 1)
            else: 
                print(self.pointsAll)
                self.pointsAll[self.actions[-1][2] - 1] = self.actions[-1][0]

                self.delRow(self.actions[-1][2])
                self.addRow(self.actions[-1][0][0], 
                            self.actions[-1][0][1],
                            self.actions[-1][0][2],
                            self.actions[-1][2] - 1)
                
            self.actions.pop(-1)

            self.canvas.update()

    def changeCommand(self):

        xValue = self.xLineEdit.text()
        yValue = self.yLineEdit.text()
        setNum = self.setNumLineEdit.text()
        pointNum = self.pointNumLineEdit.text()


        if len(pointNum) == 0:
            msg = MessageBox("Ошибка",
                             "Точка не выбрана!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        try:
            pointNum = int(pointNum)
        except:
            msg = MessageBox("Ошибка",
                             "Введены некорректные данные!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return

        if not (1 <= pointNum <= len(self.pointsAll)):
            msg = MessageBox("Ошибка",
                             "Нет доступной точки!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        try:
            if len(xValue) != 0:
                xValue = float(xValue)
            if len(yValue) != 0:
                yValue = float(yValue)
            if len(setNum) != 0:
                setNum = int(setNum)
        except:
            msg = MessageBox("Ошибка",
                             "Некорректные данные!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        oldPoint = self.pointsAll[pointNum - 1].copy()

        if len(str(xValue)) != 0:
            self.pointsAll[pointNum - 1][0] = xValue 
        
        if len(str(yValue)) != 0:
            self.pointsAll[pointNum - 1][1] = yValue

        if len(str(setNum)) != 0:
            self.pointsAll[pointNum - 1][2] = setNum

        self.actions.append((oldPoint, self.pointsAll[pointNum - 1], pointNum, "change"))
        
        self.delRow(pointNum)
        self.addRow(self.pointsAll[pointNum - 1][0],
                    self.pointsAll[pointNum - 1][1], 
                    self.pointsAll[pointNum - 1][2], 
                    pointNum - 1)

        self.canvas.update()
        
    def addCommand(self):

        xValue = self.xLineEdit.text()
        yValue = self.yLineEdit.text()
        setNum = self.setNumLineEdit.text()

        text = "Пустое поле "

        if len(xValue) == 0:
            text += "\"X\"!"
        elif len(yValue) == 0:
            text += "\"Y\"!"
        elif len(setNum) == 0:
            text += "\"Множество\"!"

        if text != "Пустое поле ":
            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        try:
            xValue = float(xValue)
            yValue = float(yValue)
            setNum = int(setNum)
        except:
            msg = MessageBox("Ошибка",
                             "Введены некорректные данные!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        if setNum != 1 and setNum != 2:
            msg = MessageBox("Ошибка",
                             "Неверный номер множества!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return

        self.actions.append([xValue, yValue, setNum, 'add'])
        self.pointsAll.append([xValue, yValue, setNum])
        self.addRow(xValue, yValue, setNum)

        newMaxValue = max(abs(xValue), abs(yValue), self.canvas.maxValue)
        if newMaxValue != self.canvas.maxValue:
            self.canvas.maxValue = self.canvas.frame * newMaxValue

        xValue, yValue = self.canvas.toCanvas([xValue, yValue])        
        
        self.canvas.update()

        self.xLineEdit.setText("")
        self.yLineEdit.setText("")
        self.setNumLineEdit.setText("")

    def delCommand(self):

        pointNum = self.pointNumLineEdit.text()

        text = "Пустое поле "

        if len(pointNum) == 0:
            text += "\"№ точки\"!"

        if text != "Пустое поле ":
            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        try:
            pointNum = int(pointNum)
        except:
            msg = MessageBox("Ошибка",
                             "Некорректные данные!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        if 1 <= pointNum <= self.tableWidget.rowCount():
            
            point = self.pointsAll.pop(pointNum - 1)
            
            self.actions.append(point + [pointNum, "del"])
            self.delRow(pointNum)
            self.canvas.update()

            self.pointNumLineEdit.setText("")
        else:
            msg = MessageBox("Ошибка",
                             "Нет доступной точки!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return

    # функции для обработки таблицы
    def styleTable(self):

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Координаты", "Множество"])

        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 260)

    def addRow(self, xValue, yValue, setNum, row = 0):

        if row == 0:
            curRow = self.tableWidget.rowCount()
        else:
            curRow = row

        self.tableWidget.insertRow(curRow)

        self.tableWidget.setItem(curRow, 0, QtWidgets.QTableWidgetItem("{:.1f}, {:.1f}".format(xValue, yValue)))
        self.tableWidget.setItem(curRow, 1, QtWidgets.QTableWidgetItem(str(setNum)))

    def delRow(self, pointNum):

        self.tableWidget.removeRow(pointNum - 1)
    
    def printProgInfo(self):
        text = "На плоскости заданы 2 множества точек. " + \
            "Найти пару окружностей, каждая из которых проходит " + \
            "хотя бы через 3 различные точки одного и того же " + \
            "множества (окружности пары строятся на точках " + \
            "разных множеств) таких, что разность площадей " + \
            "четырехугольников, образованных центрами окружностей, " + \
            "точками внутренних общих касательных и точкой пересечения " + \
            "касательных, максимальна."
        
        msg = MessageBox("Об программе", 
                         text, 
                         QtWidgets.QMessageBox.Information)
        
        msg.show()

    def printAuthorInfo(self):
        msg = MessageBox("Об авторе", 
                         "Савинова Мария\nИУ7-41Б", 
                         QtWidgets.QMessageBox.Information)
        
        msg.show()

    def exitProgram(self):
        sys.exit()

class MessageBox(QtWidgets.QMessageBox):

    def __init__(self, title, text, icon):
        super().__init__()

        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(icon)
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def show(self):
        x = self.exec_()

class Canvas(QtWidgets.QWidget):
    
    def __init__(self, parent, addRow, pointsAll, actions, solution):
        super().__init__(parent)

        self.setMouseTracking(True)

        self.penFirst = QtGui.QPen(Qt.red, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.penSecond = QtGui.QPen(Qt.green, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

        self.painter = QtGui.QPainter()

        self.addRow = addRow

        self.resPointsFirst = list()  
        self.resPointsSecond = list() 

        self.pointsAll = pointsAll    # информация о всех точках
        self.actions = actions

        self.maxValue = 10.0
        self.scale = -1
        self.frame = 1.05

        self.solution = solution

    def toCanvas(self, point: list): # из фактических в канвас
        
        xValue = int(self.width() // 2 + point[0] / self.scale)
        yValue = int(self.height() // 2 - point[1] / self.scale)

        return [xValue, yValue]
    
    def fromCanvas(self, point: list): # из канваса в фактические

        xValue = (point[0] - self.width() // 2) * self.scale
        yValue = (-point[1] + self.height() // 2) * self.scale

        return [xValue, yValue]

    def paintEvent(self, event):

        self.painter.begin(self)

        self.scale = 2 * self.maxValue / min(self.width(), self.height())

        self.painter.fillRect(0, 0, self.width(), self.height(), Qt.white)

        pen = QtGui.QPen(Qt.black, 1)

        self.painter.setPen(pen)
        self.painter.drawLine(QtCore.QPoint(self.width()//2, 0), QtCore.QPoint(self.width()//2, self.height()))
        self.painter.drawLine(QtCore.QPoint(0, self.height()//2), QtCore.QPoint(self.width(), self.height()//2))
        
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, self.height() // 2 - 5), "(0.0, 0.0)")
        self.painter.drawText(QtCore.QPoint(self.width() - 85, self.height() // 2 - 5), "({:.1f}, 0.0)".format(self.maxValue))
        self.painter.drawText(QtCore.QPoint(0, self.height() // 2 - 5), "(-{:.1f}, 0.0)".format(self.maxValue))
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, 20), "(0.0, {:.1f})".format(self.maxValue))
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, self.height()), "(0.0, {:.1f})".format(self.maxValue))

        i = 1
        for point in self.pointsAll:
            if point[2] == 1:
                self.painter.setPen(self.penFirst)
            else:
                self.painter.setPen(self.penSecond)

            xValue, yValue = self.toCanvas(point)

            drawPoint = QtCore.QPoint(xValue, yValue)

            self.painter.drawPoint(drawPoint)
            self.painter.drawText(drawPoint, " {}.({:.1f}, {:.1f})".format(i, point[0], point[1]))
            
            i += 1

        if len(self.solution):
            pass

            #TODO решение

            # for i in range(len(self.solution)):
            #     self.painter.drawEllipse()

        self.painter.end()

    def mousePressEvent(self, event):

        setNum = 0

        if event.type() == QtCore.QEvent.MouseButtonPress:

            point = event.pos()

            if event.button() == QtCore.Qt.LeftButton:
                setNum = 1
            else:
                setNum = 2

            xValue, yValue = self.fromCanvas([point.x(), point.y()])

            newMaxValue = max(abs(xValue), abs(yValue), self.maxValue)

            if self.maxValue != newMaxValue:
                self.maxValue = newMaxValue * self.frame

            self.scale = 2 * self.maxValue / min(self.width(), self.height())

            self.addRow(xValue, yValue, setNum) 
            self.actions.append([xValue, yValue, setNum, "add"])
            self.pointsAll.append([xValue, yValue, setNum])
            
        self.update()

    def clearCanvas(self):

        self.pixmap().fill(Qt.white)

        self.update()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()
