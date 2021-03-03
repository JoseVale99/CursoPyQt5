from PyQt5.QtWidgets import *
from View.UI.Ventana_1 import  Ui_Ventana1
from View.Subventana import Ventana2
import sys

class Principal(QDialog):

    def __init__(self):
        super(Principal, self).__init__()
        self.app = Ui_Ventana1()
        self.app.setupUi(self)
        self.ventana2  = Ventana2()
        
        self.app.btnAbrir.clicked.connect(lambda: self.ventana2.mostrar())
        self.app.btnUno.clicked.connect(lambda: self.enviarInformacion())
        self.ventana2.widgets.btnDos.clicked.connect(lambda: self.setInformacion())
    
    def enviarInformacion(self):
        datos = self.app.lineUno.text()
        self.ventana2.setInformacion(datos)

    def setInformacion(self):
        datos = self.ventana2.getDatos()
        self.app.lineUno.insert(datos)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1= Principal()
    ventana1.show()
    sys.exit(app.exec_())