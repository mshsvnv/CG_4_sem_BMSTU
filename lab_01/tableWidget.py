from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class TableWidget(QTableWidget):

    def __init__(self, place):
        super().__init__(0, 3, place)
        self.setHorizontalHeaderLabels(["X", "Y", "Множество"])
        # self.setRowCount(1)
        self.setColumnCount(3)

        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 150)
        self.setColumnWidth(2, 155)

    def addRow(self, xValue, yValue, setNum):

        curRow = self.currentRow() + 1
        self.insertRow(curRow)

        self.setItem(curRow, 0, QTableWidgetItem("{:.1f}".format(xValue)))
        self.setItem(curRow, 1, QTableWidgetItem("{:.1f}".format(yValue)))
        self.setItem(curRow, 2, QTableWidgetItem(str(setNum)))

    def delRow(self, pointNum):

        self.removeRow(pointNum - 1)
