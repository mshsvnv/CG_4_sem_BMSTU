from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_deleteWindow(object):
    def setupUi(self, deleteWindow):
        deleteWindow.setObjectName("deleteWindow")
        deleteWindow.resize(304, 120)
        self.centralwidget = QtWidgets.QWidget(deleteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 285, 98))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.xLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.xLabel.setFont(font)
        self.xLabel.setObjectName("xLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.xLabel)
        self.xLineEdit = QtWidgets.QLineEdit(self.widget)
        self.xLineEdit.setObjectName("xLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.xLineEdit)
        self.setLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setLabel.setFont(font)
        self.setLabel.setObjectName("setLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.setLabel)
        self.setLineEdit = QtWidgets.QLineEdit(self.widget)
        self.setLineEdit.setObjectName("setLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.setLineEdit)
        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setEnabled(True)
        self.deleteButton.setObjectName("deleteButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.deleteButton)
        deleteWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(deleteWindow)
        QtCore.QMetaObject.connectSlotsByName(deleteWindow)

    def retranslateUi(self, deleteWindow):
        _translate = QtCore.QCoreApplication.translate
        deleteWindow.setWindowTitle(_translate("deleteWindow", "Удалить"))
        self.xLabel.setText(_translate("deleteWindow", "X: "))
        self.setLabel.setText(_translate("deleteWindow", "Множество: "))
        self.deleteButton.setText(_translate("deleteWindow", "Удалить"))
