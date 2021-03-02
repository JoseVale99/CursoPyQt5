from PyQt5.QtWidgets import *
import sys
from Vista.qtableView import Ui_MainWindow
from PyQt5.QtGui import *


class Tabla(QMainWindow):
    def __init__(self):
        super(Tabla, self).__init__()
        self.tabla = Ui_MainWindow()
        self.tabla.setupUi(self)

        # -------------  Window Center --------------------------
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))


        # Crear modelo

        filas = 2
        columnas = 3
        model = QStandardItemModel(filas, columnas)
        header = ["Columna 1", "Columna 2", "Columna 3"]
        datos = [["Dato 1", "Dato 2", "Dato 3"],["Dato 4", "Dato 5", "Dato 6"]]

        model.setHorizontalHeaderLabels(header) 
        for fila in range(len(datos)):
            for columna in range(len(header)):
                model.setItem(fila, columna, QStandardItem(datos[fila][columna]))


        self.tabla.tableView.setModel(model)

        self.tabla.tableView.doubleClicked.connect(self.prueba)

        #self.tabla.tableView.setRowHidden(1, True)
        #print(self.tabla.tableView.isRowHidden(1))
        #print(self.tabla.tableView.model().index(0,0).data())


    def prueba(self, dato):
        print(dato.row(), dato.column())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Tabla()
    my_app.show()
    sys.exit(app.exec_())
