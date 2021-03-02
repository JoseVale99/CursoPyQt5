from PyQt5.QtWidgets import (QTableWidgetItem, QApplication,QMainWindow,
     QDesktopWidget)
from PyQt5.QtGui import  QStandardItemModel, QStandardItem
import sys,Eventos
from View.Vista import Ui_MainWindow
from Model.Cargar_Tablas import CargarTablaWidget, Cargar_TablaView


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
        # -----  Cargar tablas ----- 
        CargarTablaWidget(self.tabla.tableWidget,QTableWidgetItem)
        Cargar_TablaView(self.tabla.tableView,QStandardItemModel,QStandardItem)

        self.tabla.tableWidget.setColumnCount(4)        
        encabezados = ["ID","NOMBRE","APELLIDO","DNI"]
        self.tabla.tableWidget.setHorizontalHeaderLabels(encabezados)
               



        # ---- Eventos  -----
        self.tabla.tableWidget.cellDoubleClicked.connect(self.tableWidgetDoubleClicked)
        self.tabla.tableView.doubleClicked.connect(self.tableViewDoubleClicked)
    
    def tableWidgetDoubleClicked(self, row):
        Eventos.enviar_a_view(row,self.tabla.tableWidget,
         self.tabla.tableView,QStandardItem)
    
    def tableViewDoubleClicked(self, item):
        Eventos.enviar_a_widget(item.row(), 
        self.tabla.tableWidget, self.tabla.tableView,QTableWidgetItem)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Tabla()
    my_app.show()
    sys.exit(app.exec_())