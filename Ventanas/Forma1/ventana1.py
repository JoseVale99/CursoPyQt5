from PyQt5.QtWidgets import *
from View.Ventana_1 import Ui_Ventana1
from View.Ventana_2 import  Ui_Ventana2
import sys

class Ventana1(QDialog):

    def __init__(self):
        super(Ventana1, self).__init__()
        self.ventana1 = Ui_Ventana1()
        self.ventana1.setupUi(self)
        self.ventana2 = Ventana2()
        
        self.ventana1.btnAbrir.clicked.connect(lambda:self.ventana2.Mostrar())
        self.ventana1.btnUno.clicked.connect(self.enviarInfo)
        self.ventana2.ventana2.btnDos.clicked.connect(lambda : self.setDato())
    
    def  enviarInfo(self):
        datos = self.ventana1.lineUno.text()
        self.ventana2.setDato(datos)

    def setDato(self):
        dato = self.ventana2.getDatos()
        self.ventana1.lineUno.setText(dato)
class Ventana2(QDialog):
    def __init__(self):
        super(Ventana2, self).__init__()
        self.ventana2 = Ui_Ventana2()
        self.ventana2.setupUi(self)
    
    def Mostrar(self):
        self.show()

    def setDato(self,dato):
        self.ventana2.lineDos.insert(dato)

    def getDatos(self):
        datos = self.ventana2.lineDos.text()
        return datos

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana2 = Ventana1()
    ventana2.show()
    sys.exit(app.exec_())