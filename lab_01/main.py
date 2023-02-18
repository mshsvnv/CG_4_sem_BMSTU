from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import Qt
import sys

class UI(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        uic.loadUi("main.ui", self)

        self.pointsFirst = list()  # точки первого множества
        self.pointsSecond = list() # точки второго множества
        self.pointsAll = list()    # информация о всех точках
        self.actions = list()

        self.canvas = Canvas(self.centralwidget, self.pointsFirst, 
                             self.pointsSecond, self.addRow, 
                             self.pointsAll, self.actions)
        self.gridLayout.addWidget(self.canvas, 4, 0, 3, 4)

        self.addButton.clicked.connect(self.addCommand)
        self.delButton.clicked.connect(self.delCommand)
        self.cancelButton.clicked.connect(self.cancelCommand)
        self.changeButton.clicked.connect(self.changeCommand)

        self.exitAction.triggered.connect(self.exitProgram)
        self.progInfo.triggered.connect(self.printProgInfo)
        self.authorInfo.triggered.connect(self.printAuthorInfo)
        
        self.styleTable()

        # TODO навесить функции на кнопки

        self.show()

    def cancelCommand(self):
    
        if len(self.actions) == 0:
            msg = MessageBox("Инфо",
                             "Не было выполнено ни одно действие!", 
                             QtWidgets.QMessageBox.Information)
            msg.show()

            return
        else:
            # TODO: доделать change и починить оставшиеся
            if self.actions[-1][2] == "add":

                if self.actions[-1][1] == 1:
                    self.pointsFirst.pop(-1)
                else:
                    self.pointsSecond.pop(-1)

                self.pointsAll.pop(-1)
                self.delRow(self.tableWidget.rowCount())
                
            elif self.actions[-1][2] == "del":
                
                if self.actions[-1][1] == 1:
                    self.pointsFirst.append(self.actions[-1][0][0])
                else:
                    self.pointsSecond.append(self.actions[-1][0][0])
                
                self.pointsAll.append(self.actions[-1][0])
                self.addRow(self.actions[-1][0][0].x(),
                            self.actions[-1][0][0].y(),
                            self.tableWidget.rowCount())
            else: 
                # change
                pass

            self.actions.pop(-1)

            self.canvas.update()

    def changeCommand(self):

        xValue = self.xLineEdit.text()
        yValue = self.yLineEdit.text()
        setNum = self.setNumLineEdit.text()
        pointNum = self.pointNumLineEdit.text()

        text = "Пустое поле "

        if len(xValue) == 0:
            text += "\"X\"!"
        elif len(yValue) == 0:
            text += "\"Y\"!"
        elif len(setNum) == 0:
            text += "\"Множество\"!"
        elif len(pointNum) == 0:
            text += "\"№ точки\"!"

        if text != "Пустое поле ":
            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        try:
            xValue = int(xValue)
            yValue = int(yValue)
            setNum = int(setNum)
            pointNum = int(pointNum)
        except:
            msg = MessageBox("Ошибка",
                             "Введены некорректные данные!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        oldPoint = self.pointsAll[pointNum - 1]

        if oldPoint[1] == setNum:
            pass
            # newPoint = QtCore.QPoint(xValue, yValue)
            # self.actions.append([oldPoint[0], newPoint, setNum, "change"])


            # множество не меняем
        else:
            # множество не меняем
            pass
        
    def addCommand(self):

        # TODO: сместить координаты от границ

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
            xValue = int(xValue)
            yValue = int(yValue)
            setNum = int(setNum)
        except:
            msg = MessageBox("Ошибка",
                             "Введены некорректные данные!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        # TODO: если неверные координаты(за границы)
        
        if setNum != 1 and setNum != 2:
            msg = MessageBox("Ошибка",
                             "Неверный номер множества!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return

        point = QtCore.QPoint(xValue, yValue)

        if setNum == 1:
            self.pointsFirst.append(point)
        else:
            self.pointsSecond.append(point)
        
        self.actions.append([point, setNum, 'add'])
        self.pointsAll.append([point, setNum])

        self.addRow(xValue, yValue, setNum)
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
            setNum = self.tableWidget.item(pointNum - 1, 1).text()

            if int(setNum) == 1:
                self.pointsFirst.remove(point[0])
            else:
                self.pointsSecond.remove(point[0])
                
            self.actions.append([point, setNum, "del"])
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

        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 140)

    def addRow(self, xValue, yValue, setNum):

        curRow = self.tableWidget.rowCount()
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
    
    def __init__(self, parent, pointsFirst, pointsSecond, addRow, pointsAll, actions):
        super().__init__(parent)

        self.setMouseTracking(True)

        self.penFirst = QtGui.QPen(Qt.red, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.penSecond = QtGui.QPen(Qt.green, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

        self.painter = QtGui.QPainter()

        self.addRow = addRow

        self.resPointsFirst = list()  
        self.resPointsSecond = list() 

        self.pointsFirst = pointsFirst   # точки первого множества
        self.pointsSecond = pointsSecond # точки второго множества

        self.pointsAll = pointsAll    # информация о всех точках
        self.actions = actions

    def paintEvent(self, event):

        self.painter.begin(self)

        self.painter.fillRect(0, 0, self.width(), self.height(), Qt.white)

        pen = QtGui.QPen(Qt.black, 1)
        self.painter.setPen(pen)
        self.painter.drawLine(QtCore.QPoint(self.width()//2, 0), QtCore.QPoint(self.width()//2, self.height()))
        self.painter.drawLine(QtCore.QPoint(0, self.height()//2), QtCore.QPoint(self.width(), self.height()//2))
        
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, self.height() // 2 - 5), "(0.0, 0.0)")
        self.painter.drawText(QtCore.QPoint(self.width() - 85, self.height() // 2 - 5), "(100.0, 0.0)")
        self.painter.drawText(QtCore.QPoint(0, self.height() // 2 - 5), "(-100.0, 0.0)")
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, 20), "(0.0, 100.0)")
        self.painter.drawText(QtCore.QPoint(self.width() // 2 + 10, self.height()), "(0.0, -100.0)")
        
        i = 1
        for point in self.pointsAll:
            if point[1] == 1:
                self.painter.setPen(self.penFirst)
            else:
                self.painter.setPen(self.penSecond)

            self.painter.drawPoint(point[0])
            self.painter.drawText(point[0], "{}.({}, {})".format(i, point[0].x(), point[0].y()))
            i += 1

        self.painter.end()

    def mousePressEvent(self, event):
        setNum = 0
        if event.type() == QtCore.QEvent.MouseButtonPress:

            point = event.pos()

            if event.button() == QtCore.Qt.LeftButton:
                self.pointsFirst.append(point)
                setNum = 1
            else:
                self.pointsSecond.append(point)
                setNum = 2

            self.addRow(point.x(), point.y(), setNum) 
            self.actions.append([point, setNum, "add"])
            self.pointsAll.append([point, setNum])
            
        self.update()

    def clearCanvas(self):

        self.pixmap().fill(Qt.white)

        self.update()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()
