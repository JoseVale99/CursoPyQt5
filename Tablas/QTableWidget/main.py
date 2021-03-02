from PyQt5.QtWidgets import *
import sys
from Vista.ui_qtablewidget import Ui_MainWindow
from PyQt5.Qt import *


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

        datos = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]

        self.tabla.tableWidget.setColumnCount(3)
        self.tabla.tableWidget.setRowCount(len(datos))
        for row in range(len(datos)):
            for column in range(len(datos[row])):
                self.tabla.tableWidget.setItem(
                    row, column, QTableWidgetItem(str(datos[row][column])))

        self.tabla.tableWidget.cellClicked.connect(self.ViewItem)
        self.tabla.tableWidget.sortItems(0, order=Qt.DescendingOrder)

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
