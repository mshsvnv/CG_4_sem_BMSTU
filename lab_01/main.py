from PyQt5 import QtWidgets, QtGui, uic
import sys
from canvas import Canvas

import itertools as it
import calcAlg

class UI(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        uic.loadUi("main.ui", self)

        self.pointsAll = list()    # информация о всех точках
        self.actions = list()      # информация о всех действиях
        self.solution = list()     # решение
        self.maxDeltaSquare = -1

        self.canvas = Canvas(self.canvasWidget, self.addRow, 
                             self.curCoordLabel, self.pointsAll, 
                             self.actions, self.solution)
        self.gridLayout.addWidget(self.canvas, 6, 0, 4, 4)

        self.addButton.clicked.connect(self.addCommand)
        self.delButton.clicked.connect(self.delCommand)
        self.cancelButton.clicked.connect(self.cancelCommand)
        self.changeButton.clicked.connect(self.changeCommand)
        self.solveButton.clicked.connect(self.solveCommand)
        self.restartButton.clicked.connect(self.restartCommand)
        self.plusButton.clicked.connect(self.scaleCommand)
        self.minusButton.clicked.connect(self.scaleCommand)

        self.exitAction.triggered.connect(self.exitProgram)
        self.progInfo.triggered.connect(self.printProgInfo)
        self.authorInfo.triggered.connect(self.printAuthorInfo)
        
        self.styleTable()

        self.show()

    def scaleCommand(self):

        name = str(self.sender().objectName())
        
        if name == "plusButton":
            self.canvas.maxValue /= 1.5
        else:
            self.canvas.maxValue *= 1.5

        self.canvas.update()

    def restartCommand(self):

        for i in range(len(self.pointsAll)):
            self.delRow(1)

        self.maxDeltaSquare = -1

        self.pointsAll = []
        self.canvas.pointsAll = self.pointsAll

        self.solution = []
        self.canvas.solution = self.solution

        self.actions = []
        self.canvas.actions = self.actions
        
        self.canvas.maxValue = 10.0
        self.canvas.scale = 2 * self.canvas.maxValue / min(self.width(), self.height())

        self.solveLabel.setText("Ответ: ")

        self.xLineEdit.setText("")
        self.yLineEdit.setText("")
        self.setNumLineEdit.setText("")
        self.pointNumLineEdit.setText("")

        self.canvas.update()

    def solveCommand(self):

        if len(self.pointsAll) ==  0:
            msg  = MessageBox("Ошибка",
                             "Нет доступных точек для построения",
                             QtWidgets.QMessageBox.Information)

            x = msg.exec_()

            return

        firstPoints = list()
        secondPoints = list()

        for i in range(len(self.pointsAll)):
            if self.pointsAll[i][-1] == 1:
                firstPoints.append(self.pointsAll[i] + [i])
            else:
                secondPoints.append(self.pointsAll[i] + [i])

        if len(firstPoints) < 3:
            msg = MessageBox("Ошибка",
                             "Недостаточно точек 1го множества",
                             QtWidgets.QMessageBox.Information)

            x = msg.exec_()

            return
        
        if len(secondPoints) < 3:
            msg = MessageBox("Ошибка",
                             "Недостаточно точек 2го множества",
                             QtWidgets.QMessageBox.Information)

            x = msg.exec_()

            return
        
        circlesFirst = list()
        circlesSecond = list()

        for points in it.combinations(firstPoints, 3):
            value = calcAlg.oneLine(points[0], points[1], points[2])

            if value:
                pass
                # print("На одной")
            else:
                centerPoint = calcAlg.circleCenter(points[0], points[1], points[2]) # в фактических координатах
                
                radius = calcAlg.lenBetwPoints(points[0], centerPoint) # в фактических координатах
                
                # print([centerPoint, radius, points[0][-1], points[1][-1], points[2][-1]])
                circlesFirst.append([centerPoint, radius, points[0][-1], points[1][-1], points[2][-1]])

                # print("Не на одной")

        if len(circlesFirst) == 0:
            msg = MessageBox("Ошибка",
                            "Из точек первого множества нельзя построить окружности",
                            QtWidgets.QMessageBox.Information)

            x = msg.exec_()

            return

        for points in it.combinations(secondPoints, 3):
            value = calcAlg.oneLine(points[0], points[1], points[2])

            if value:
                pass
                # print("На одной")
            else:
                centerPoint = calcAlg.circleCenter(points[0], points[1], points[2]) # в фактических координатах
                
                radius = calcAlg.lenBetwPoints(points[0], centerPoint) # в фактических координатах

                # print([centerPoint, radius, points[0][-1], points[1][-1], points[2][-1]])
                circlesSecond.append([centerPoint, radius, points[0][-1], points[1][-1], points[2][-1]])

                # print("Не на одной")

        if len(circlesFirst) == 0:
            msg = MessageBox("Ошибка",
                            "Из точек второго множества нельзя построить окружности",
                            QtWidgets.QMessageBox.Information)

            x = msg.exec_()

            return
                
        for i in range(len(circlesFirst)):
            for j in range(len(circlesSecond)):

                spaceBetwCenters = calcAlg.lenBetwPoints(circlesFirst[i][0],
                                                         circlesSecond[j][0])
                
                if spaceBetwCenters > circlesFirst[i][1] + circlesSecond[j][1]: # окружности не пересекаются и не касаются
            
                    interPoint = calcAlg.interPointCoord(circlesFirst[i][1], 
                                                         circlesFirst[i][0],
                                                         circlesSecond[j][1],
                                                         circlesSecond[j][0])
                    
                    p_3First, p_4First = calcAlg.circlesIntersection(circlesFirst[i], interPoint)  # координаты точек персечения окружностей
                    p_3Second, p_4Second = calcAlg.circlesIntersection(circlesSecond[j], interPoint)
                    
                    squareFirst = calcAlg.triangleSquare(circlesFirst[i][0], 
                                                         p_3First, 
                                                         interPoint)

                    squareSecond = calcAlg.triangleSquare(circlesSecond[j][0], 
                                                         p_3Second, 
                                                         interPoint)

                    curDeltaSquare = abs(squareFirst - squareSecond)

                    if curDeltaSquare >= self.maxDeltaSquare:
                        self.actions.append([self.canvas.maxValue, self.maxDeltaSquare, "draw"])
                        self.maxDeltaSquare = curDeltaSquare                    
                        
                        self.solution = [circlesFirst[i] + p_3First + p_4First]
                        self.solution.append(circlesSecond[j] + p_3Second + p_4Second) 
                        self.solution.append(interPoint)

                        self.canvas.solution = self.solution
                        
                        maxValue = []
                        for k in range(2):
                            maxValue += [circlesFirst[i][0][k] - circlesFirst[i][1],
                                            circlesFirst[i][0][k] + circlesFirst[i][1],
                                            circlesSecond[j][0][k] - circlesSecond[j][1],
                                            circlesSecond[j][0][k] + circlesSecond[j][1]]

                        maxValue = [abs(x) for x in maxValue]

                        self.canvas.maxValue = max(maxValue)

                        # self.canvas.maxValue = max(max(maxValue), self.canvas.maxValue)
                        
                        text = "Ответ: \nМакисмальная разность площадей: {:.3f}".format(self.maxDeltaSquare)
                        text += "\nТочки первого множества:\n"
                        for k in range(3):
                            text += "{}. ({:.1f}, {:.1f}); ".format(
                                circlesFirst[i][k + 2] + 1, 
                                self.pointsAll[circlesFirst[i][k + 2]][0],
                                self.pointsAll[circlesFirst[i][k + 2]][1])
                        
                        text += "\n\nТочки второго множества:\n"
                        for k in range(3):
                            text += "{}. ({:.1f}, {:.1f}); ".format(
                                circlesSecond[j][k + 2] + 1, 
                                self.pointsAll[circlesSecond[j][k + 2]][0],
                                self.pointsAll[circlesSecond[j][k + 2]][1])
                            
                        self.solveLabel.setText(text)

        if len(self.solution) == 0:
            msg = MessageBox("Ошибка",
                             "Подходящих окружностей нет!", 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        self.canvas.update()
        
        self.solution = list()
        self.maxDeltaSquare = -1

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
            elif self.actions[-1][-1] == "change": 
                self.pointsAll[self.actions[-1][2] - 1] = self.actions[-1][0]

                self.delRow(self.actions[-1][2])
                self.addRow(self.actions[-1][0][0], 
                            self.actions[-1][0][1],
                            self.actions[-1][0][2],
                            self.actions[-1][2] - 1)
            else:
                self.canvas.maxValue = self.actions[-1][0]
                self.maxDeltaSquare = self.actions[-1][1]
                self.solution = []
                self.canvas.solution = []
                
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
            if setNum == 1 or setNum == 2:
                self.pointsAll[pointNum - 1][2] = setNum
            else:
                msg = MessageBox("Ошибка",
                                    "Неверный номер множества!", 
                                    QtWidgets.QMessageBox.Warning)
                msg.show()

                return


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

        self.canvas.maxValue = max(abs(xValue), abs(yValue), self.canvas.maxValue)
        
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
        
        self.tableWidget.setFont(QtGui.QFont('Ubuntu', 15))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Координаты", "Множество"])

        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 260)


    def addRow(self, xValue, yValue, setNum, row = -1):

        if row == -1:
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
        
        msg = MessageBox("О программе", 
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
        self.setFont(QtGui.QFont("Ubuntu", 15))
        self.setGeometry(300, 300, 500, 500)
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def show(self):
        x = self.exec_()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()
