from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from canvas import Canvas

class UI(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi("main.ui", self)

        self.canvas = Canvas(self.canvasWidget)
        self.gridLayout.addWidget(self.canvas, 8, 0, 7, 3)

        self.rotateButton.clicked.connect(self.rotateCommand)
        self.moveButton.clicked.connect(self.moveCommand)
        self.scaleButton.clicked.connect(self.scaleCommand)

        self.cancelButton.clicked.connect(self.cancelCommand)
        self.restartButton.clicked.connect(self.restartCommand)
        self.pointButton.clicked.connect(self.pointInfo)

        self.plusButton.clicked.connect(self.scaleCommand)
        self.minusButton.clicked.connect(self.scaleCommand)

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
        y = self.xLineEdit.text()

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
        
        self.angleLineEdit.setText("")
        self.xLineEdit.setText("")
        self.yLineEdit.setText("")

        # функция поворота
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

        # перемещение точек

        self.dxLineEdit.setText("")
        self.dyLineEdit.setText("")
        self.xLineEdit.setText("")
        self.yLineEdit.setText("")

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
        
        self.kxLineEdit.setText("")
        self.kyLineEdit.setText("")
        
        self.xLineEdit.setText("")
        self.yLineEdit.setText("")
        
        # функция масштабирования
        self.canvas.update()

    def cancelCommand(self):
        # отмена последнего действия
        pass

    def restartCommand(self):
        # сброс всех данных и возврат к началу
        pass

    def scaleCommand(self):
        name = str(self.sender().objectName())
        
        if name == "plusButton":
            self.canvas.maxValue *= 1.5
        else:
            self.canvas.maxValue /= 1.5

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