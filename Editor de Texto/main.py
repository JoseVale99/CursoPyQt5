from  PyQt5.QtWidgets import QMainWindow, QApplication, \
    QMessageBox, QFileDialog,QDesktopWidget
from Vista.View import Ui_MainWindow
import  sys, eventos
from PyQt5.QtGui import  QCloseEvent
from Desing.Style import  style
class Editor(QMainWindow):
    def __init__(self):
        super(Editor,self).__init__()
        self.editor = Ui_MainWindow()
        self.editor.setupUi(self) 
        self.setStyleSheet(style)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), 
        int((screen.height() - size.height())/2)) 

        self.title = "Editor de texto"
        self.control = 0
        self.ruta = ""

        # ---- Eventos propios   ----
        self.editor.textEdit.textChanged.connect(self.textChanged)

        # ---- Eventos externos ----
        self.editor.actionAbrir.triggered.connect(lambda:self.abrirArchivo())
        self.editor.actionGuardar_como.triggered.connect(lambda: self.GuardarArchivo())
        self.editor.actionNuevo.triggered.connect(self.ArchivoNuevo)

    def textChanged(self):
        if self.title == "Editor de texto" or self.title == "Editor de texto - *":
            self.setWindowTitle("Editor de texto - *")
        else:
            self.setWindowTitle(self.title +" *")
        self.control =1

    def abrirArchivo(self):
        control = self.validar(2)
        if control:
            self.ruta = eventos.Abir_archivo(
                QFileDialog(), self.editor.textEdit,self)
            self.title = f"Editor de texto - {self.ruta}"
            self.title = "Editor de texto"
            self.control = 0
        
    def ArchivoNuevo(self):
        control = self.validar(1)
        if control:
            self.editor.textEdit.setText("")
            self.setWindowTitle("Editor de texto")
            self.control = 0

    def GuardarArchivo(self):
        aux = self.ruta 

        self.ruta = eventos.GuardarComo(
        QFileDialog(), self.editor.textEdit,self
        )
        if aux != self.ruta:
            self.title = f"Editor de texto - {self.ruta}"
            self.control = 0

    def validar(self, parametro):
        if self.control:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Alerta")
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            btnYes = msgbox.button(QMessageBox.Yes).setText("SI")
            
            if parametro == 1:
                msgbox.setText(
                "Estas por crear un nuevo arhivo, se va a eliminar el contenido modificado, ¿Desea continuar?")
            elif parametro ==2:
                msgbox.setText(
                "Estas por abrir otro arhivo, se va a eliminar el contenido modificado, ¿Desea continuar?")
            elif parametro == 3:
                msgbox.setText("Estas por cerrar el programa sin guardar cambios, ¿desea continuar?")
            
            respuesta = msgbox.exec_()
            if respuesta == QMessageBox.Yes:
                return 1
            else:
                return 0
        else:
            return 1
    
    def closeEvent(self, event):
        control = self.validar(3)
        if control:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Editor()
    my_app.show()
    sys.exit(app.exec_())