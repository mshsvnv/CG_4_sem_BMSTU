from PyQt5 import QtGui, QtWidgets, uic
import sys
from canvas import Canvas

#TODO cancel add point + debug

class UI(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi("main.ui", self)

        self.actions = list()

        self.canvas = Canvas(self.canvasWidget, self.xLineEdit, self.yLineEdit)
        self.gridLayout.addWidget(self.canvas, 9, 0, 7, 3)

        self.rotateButton.clicked.connect(self.rotateCommand)
        self.moveButton.clicked.connect(self.moveCommand)
        self.scaleButton.clicked.connect(self.scaleCommand)

        self.cancelButton.clicked.connect(self.cancelCommand)
        self.restartButton.clicked.connect(self.restartCommand)
        self.pointButton.clicked.connect(self.pointInfo)

        self.plusButton.clicked.connect(self.scaleCanvasCommand)
        self.minusButton.clicked.connect(self.scaleCanvasCommand)

        self.exit.triggered.connect(self.exitProgram)
        self.progInfo.triggered.connect(self.printProgInfo)
        self.authorInfo.triggered.connect(self.printAuthorInfo)
        
        self.show()
    
    @staticmethod
    def pointInfo():
        text = "Ключевая точка - точка, относительно которой " + \
            "производятся поворот и масштаб"
        
        msg = MessageBox("О программе",
                         text,
                         QtWidgets.QMessageBox.Information)
        
        msg.show()

    @staticmethod
    def printProgInfo():
        text = "Нарисовать исходный рисунок.\nОсуществить " + \
            "возможность его перемещения, масштабирования, поворота."
        
        msg = MessageBox("О программе",
                         text,
                         QtWidgets.QMessageBox.Information)
        
        msg.show()

    @staticmethod
    def printAuthorInfo():
        text = "Савинова Мария\nИУ7-41Б"
        msg = MessageBox("Об авторе",
                         text,
                         QtWidgets.QMessageBox.Information)
        
        msg.show()

    @staticmethod
    def exitProgram():
        sys.exit()

    def getmainPointCoords(self):
        x = self.xLineEdit.text()
        y = self.yLineEdit.text()

        if len(x) == 0 or len(y) == 0:
            text = "Не выбрана ключевая точка!"

            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return None, None
        
        try:
            x = float(x)
            y = float(y)
        except:
            text = "Неверные значения координат!"

            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return None, None
        
        return [x, y]

    def rotateCommand(self):

        x, y = self.getmainPointCoords()

        if x is None and y is None:
            return
        
        angle = self.angleLineEdit.text()

        if len(angle) == 0:
            text = "Не введено значение угла!"

            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return 
        
        try:
            angle = float(angle)
        except:
            text = "Неверное значение угла!"

            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return

        self.actions.append([x, y, -1 * angle, "rotate"])
        self.canvas.rotatePoints(x, y, angle)
        self.canvas.update()

    def moveCommand(self):
        
        dx = self.dxLineEdit.text()
        dy = self.dyLineEdit.text()

        if len(dx) == 0 or len(dy) == 0:
            text = "Не введены значения смещения!"

            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return 
        
        try:
            dx = float(dx)
            dy = float(dy)
        except:
            text = "Неверные значения смещения!"

            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        self.actions.append([-1 * dx, -1 * dy, "move"])
        self.canvas.movePoints(dx, dy)
        self.canvas.update()

    def scaleCommand(self):

        x, y = self.getmainPointCoords()

        if x is None and y is None:
            return
    
        kx = self.kxLineEdit.text()
        ky = self.kyLineEdit.text()

        if len(kx) == 0 or len(ky) == 0:
            text = "Не введен к-т масштабирования!"

            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return 
        
        try:
            kx = float(kx)
            ky = float(ky)
        except:
            text = "Неверное значение к-та!"

            msg = MessageBox("Ошибка",
                             text, 
                             QtWidgets.QMessageBox.Warning)
            msg.show()

            return
        
        self.actions.append([x, y, 1 / kx, 1 / ky, "scale"])
        self.canvas.scalePoints(x, y, kx, ky)
        self.canvas.update()

    def cancelCommand(self):

        print(self.actions)
        
        if len(self.actions) == 0:
            text = "Не выполнено ни одно действие!"

            msg = MessageBox("Информация",
                             text, 
                             QtWidgets.QMessageBox.Information)
            msg.show()

            return

        if self.actions[-1][-1] == "move":
            self.canvas.movePoints(self.actions[-1][0], 
                                   self.actions[-1][1])
            
        elif self.actions[-1][-1] == "scale":
            self.canvas.scalePoints(self.actions[-1][0], 
                                   self.actions[-1][1],
                                   self.actions[-1][2], 
                                   self.actions[-1][3])
        else:
            self.canvas.rotatePoints(self.actions[-1][0], 
                                   self.actions[-1][1],
                                   self.actions[-1][2])

        self.actions.pop()

        self.canvas.update()
    
    def restartCommand(self):

        self.canvas.maxValue = 3.0
        self.canvas.mainPoint = None

        self.angleLineEdit.setText("")

        self.dxLineEdit.setText("")
        self.dyLineEdit.setText("")

        self.kxLineEdit.setText("")
        self.kyLineEdit.setText("")

        self.xLineEdit.setText("")
        self.yLineEdit.setText("")
        
        self.canvas.makeGraph()
        self.canvas.update()

    def scaleCanvasCommand(self):
        name = str(self.sender().objectName())
        
        if name == "plusButton":
            self.canvas.maxValue /= 1.5
        else:
            self.canvas.maxValue *= 1.5

        self.canvas.update()

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