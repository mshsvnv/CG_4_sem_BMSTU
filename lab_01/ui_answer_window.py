from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_answerWindow(object):

    def setupUi(self, answerWindow):
        answerWindow.setObjectName("answerWindow")
        answerWindow.resize(642, 188)
        self.centralwidget = QtWidgets.QWidget(answerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 631, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cancelTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.cancelTextEdit.setObjectName("cancelTextEdit")
        self.verticalLayout.addWidget(self.cancelTextEdit)
        self.cancleButton = QtWidgets.QPushButton(self.widget)
        self.cancleButton.setObjectName("cancleButton")
        self.verticalLayout.addWidget(self.cancleButton)
        answerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(answerWindow)
        QtCore.QMetaObject.connectSlotsByName(answerWindow)

    def retranslateUi(self, answerWindow):
        _translate = QtCore.QCoreApplication.translate
        answerWindow.setWindowTitle(_translate("answerWindow", "Ответ"))
        self.cancleButton.setText(_translate("answerWindow", "Отмена"))
