from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt

# class GraphicsView(QGraphicsView):

#     scene = QGraphicsScene()

#     def __init__(self, place):

#         super().__init__(GraphicsView.scene, place)

#         self.setGeometry(QtCore.QRect(540, 30, 981, 961))
#         self.setMouseTracking(True)

#         self.viewport().installEventFilter(self)

#     def eventFilter(self, source, event):

#         if event.type() == QtCore.QEvent.MouseButtonPress:
#             if event.button() == QtCore.Qt.LeftButton:
#                 print(event.x(), event.y())
#             else:
#                 print(event.x(), event.y())

#         GraphicsView.scene.add

#         return super(GraphicsView, self).eventFilter(source, event)

#     def cleanScene(self):
#         pass

#     def drawSolve(self):
#         pass

# class GraphicsScene(QGraphicsScene):

#     def __init__(self):