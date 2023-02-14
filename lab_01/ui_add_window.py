from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_addWindow(object):

    def setupUi(self, addWindow):

        font = QtGui.QFont()
        font.setPointSize(15)

        addWindow.setObjectName("addWindow")
        addWindow.resize(300, 150)
        self.centralwidget = QtWidgets.QWidget(addWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 285, 132))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.xLineEdit = QtWidgets.QLineEdit(self.widget)
        self.xLineEdit.setObjectName("xLineEdit")
        self.gridLayout.addWidget(self.xLineEdit, 0, 1, 1, 1)

        self.setLineEdit = QtWidgets.QLineEdit(self.widget)
        self.setLineEdit.setObjectName("setLineEdit")
        self.gridLayout.addWidget(self.setLineEdit, 2, 1, 1, 1)

        self.setLabel = QtWidgets.QLabel(self.widget)
        self.setLabel.setFont(font)
        self.setLabel.setObjectName("setLabel")
        self.gridLayout.addWidget(self.setLabel, 2, 0, 1, 1)

        self.yLineEdit = QtWidgets.QLineEdit(self.widget)
        self.yLineEdit.setObjectName("yLineEdit")
        self.gridLayout.addWidget(self.yLineEdit, 1, 1, 1, 1)

        self.xLabel = QtWidgets.QLabel(self.widget)
        self.xLabel.setFont(font)
        self.xLabel.setObjectName("xLabel")
        self.gridLayout.addWidget(self.xLabel, 0, 0, 1, 1)

        self.yLabel = QtWidgets.QLabel(self.widget)
        self.yLabel.setFont(font)
        self.yLabel.setObjectName("yLabel")
        self.gridLayout.addWidget(self.yLabel, 1, 0, 1, 1)

        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setEnabled(True)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 3, 1, 1, 1)
        addWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(addWindow)
        QtCore.QMetaObject.connectSlotsByName(addWindow)

    def retranslateUi(self, addWindow):
        _translate = QtCore.QCoreApplication.translate
        addWindow.setWindowTitle(_translate("addWindow", "Добавить"))
        self.setLabel.setText(_translate("addWindow", "Множество: "))
        self.xLabel.setText(_translate("addWindow", "X: "))
        self.yLabel.setText(_translate("addWindow", "Y: "))
        self.addButton.setText(_translate("addWindow", "Добавить"))

