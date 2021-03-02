from PyQt5.QtWidgets import QTableWidgetItem, QApplication,QMainWindow, QDesktopWidget
import sys
from View.ui_qtablewidget import Ui_MainWindow
from  Model.conexion import DataBase
from  Model.Cargar_Datos import CargarTabla
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

        connection = DataBase()
        CargarTabla(self.tabla.tableWidget,QTableWidgetItem)
        #data = connection.getData()
       

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


