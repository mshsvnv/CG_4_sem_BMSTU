from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt

class GraphicsView(QGraphicsView):

    def __init__(self, place):
        super().__init__(place)

        self.setGeometry(QtCore.QRect(540, 30, 981, 961))
        self.setMouseTracking(True)

        self.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        scene = QGraphicsScene()
        redBrush = QBrush(Qt.red)
        blueBrush = QPen(Qt.blue)

        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                print(event.x(), event.y())
                ellipse = scene.addEllipse(event.x(), event.y(), 5, 5, blueBrush, redBrush)
            else:
                print(event.x(), event.y())
                ellipse = scene.addEllipse(event.x(), event.y(), 5, 5, blueBrush, redBrush)

        self.view = QGraphicsView(scene, self)
        
        return super(GraphicsView, self).eventFilter(source, event)
    
    def drawAxis(self):
        pass

    def cleanScene(self):
        pass

    def drawSolve(self):
        pass