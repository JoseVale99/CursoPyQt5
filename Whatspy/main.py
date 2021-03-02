from PyQt5.QtWidgets import (QApplication,
    QMainWindow,QSizeGrip)
import  sys, events
from  View.Vista import  Ui_MainWindow
from PyQt5.QtCore import Qt, QPoint 
class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana,self).__init__()
        self.app = Ui_MainWindow()
        self.app.setupUi(self)
        self.dragPos = QPoint()
        self.app.btn_exportar.setEnabled(False)
        self.app.grip = QSizeGrip(self.app.Grip)
        
        # ----- Datos ------
        self.fila_num = 0
        self.fila_value = 0 


        def moverVentana(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.app.Ventana.mouseMoveEvent = moverVentana

        # Botones Ventana. 
        self.app.btn_verde.clicked.connect(lambda: self.ControlWindow())
        self.app.btn_amarillo.clicked.connect(lambda: events.minimizarVentana(self))
        self.app.btn_rojo.clicked.connect(lambda:events.cerrarVentana(self))

        # Botones funcionales
        self.app.btn_abrir.clicked.connect(lambda: self.getChat())
        self.app.btn_exportar.clicked.connect(lambda: events.exportarChat(self.fila_num, self.fila_value))


        self.control_ventana = 0
    
    def getChat(self):
        try:
            datos = events.abrirChat(self.app.tabla, self.app.btn_exportar, self.app.label)
            self.fila_num = datos[0]
            self.fila_value = datos[1]
        except:
            pass

    def ControlWindow(self):
        if self.control_ventana:
            events.normalizarVentana(self)
            self.control_ventana = 0
        else:
            events.maximizarVentana(self)
            self.control_ventana = 1           

    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Ventana()
    my_app.show()
    sys.exit(app.exec_())


