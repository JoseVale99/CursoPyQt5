from PyQt5.QtWidgets import *
import  sys, Events
from  Vista.Formulario import  Ui_MainWindow

class  Registro(QMainWindow):
    def __init__(self):
        super(Registro,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), 
        int((screen.height() - size.height())/2)) 

        self.resultado = 0    
        
        # !------Eventos
        self.ui.Edit_name.textChanged.connect(lambda: Events.getValidarText(self.ui.Edit_name))
        self.ui.Edit_ap.textChanged.connect(lambda: Events.getValidarText(self.ui.Edit_ap))
        self.ui.Edit_dir.textChanged.connect(lambda: Events.getDirecccion(self.ui.Edit_dir))
        self.ui.Edit_tel.textChanged.connect(lambda: Events.getValidarNum(self.ui.Edit_tel))
        self.ui.box_edad.textChanged.connect(lambda: Events.getValidarEdad(self.ui.box_edad))

        #! Boton Registro
        self.ui.btn_reg.clicked.connect(lambda: Events.getValidarRegistro([self.ui.Edit_name,
        self.ui.Edit_ap, self.ui.Edit_dir,self.ui.Edit_tel,self.ui.box_edad,self]))
        self.ui.btn_reg.clicked.connect(self.Alert)

    def Alert(self):
        message = QMessageBox()
        message.setWindowTitle("Alerta")
        if self.resultado == 2:
            message.setText("¡Verifica los campos!")
        else:
            message.setText("¡Registrado con éxito!")
        message.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Registro()
    my_app.show()
    sys.exit(app.exec_())


