from PyQt5.QtWidgets import *
import sys
from View.ui_qtablewidget import Ui_MainWindow
from PyQt5.Qt import *
from  Model.connection import DataBase

class Tabla(QMainWindow):
    def __init__(self):
        super(Tabla, self).__init__()
        self.tabla = Ui_MainWindow()
        self.tabla.setupUi(self)

        # centrar ventana
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))

        #self.columns = ['Columna 1','Columna 2','Columna 3']
        # self.tabla.tableWidget.setColumnCount(len(self.columns))
        # self.tabla.tableWidget.setHorizontalHeaderLabels(self.columns)

        connection = DataBase()
        data = connection.getData()

        self.tabla.tableWidget.setColumnCount(len(data[0]))
        self.tabla.tableWidget.setRowCount(len(data))
        for row in range(len(data)):
            for column in range(len(data[row])):
                self.tabla.tableWidget.setItem(
                    row, column, QTableWidgetItem(str(data[row][column])))

        self.tabla.tableWidget.cellClicked.connect(self.ViewItem)
        #self.tabla.tableWidget.sortItems(0, order=Qt.DescendingOrder)

    def ViewItem(self, row, column):
        try:
            print(self.tabla.tableWidget.item(row, column).text())
        except:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Tabla()
    my_app.show()
    sys.exit(app.exec_())


# 2.1 y 2.2
