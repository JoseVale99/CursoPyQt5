from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
import  sys, events
from  Vista.Calc import  Ui_MainWindow
from Desing.Style import style
from qtpy.QtGui import QIcon

class  Calculadora(QMainWindow):
    def __init__(self):
        super(Calculadora,self).__init__()
        self.calc = Ui_MainWindow()
        self.calc.setupUi(self)
        self.setStyleSheet(style)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), 
        int((screen.height() - size.height())/2)) 

    #! ----- Button clicked-----
        self.calc.btn_0.clicked.connect(lambda: self.functionsbtn("0"))
        self.calc.btn_1.clicked.connect(lambda: self.functionsbtn("1"))
        self.calc.btn_2.clicked.connect(lambda: self.functionsbtn("2"))
        self.calc.btn_3.clicked.connect(lambda: self.functionsbtn("3"))
        self.calc.btn_4.clicked.connect(lambda: self.functionsbtn("4"))
        self.calc.btn_5.clicked.connect(lambda: self.functionsbtn("5"))
        self.calc.btn_6.clicked.connect(lambda: self.functionsbtn("6"))
        self.calc.btn_7.clicked.connect(lambda: self.functionsbtn("7"))
        self.calc.btn_8.clicked.connect(lambda: self.functionsbtn("8"))
        self.calc.btn_9.clicked.connect(lambda: self.functionsbtn("9"))
        self.calc.btn_suma.clicked.connect(lambda: self.functionsbtn("+"))
        self.calc.btn_resta.clicked.connect(lambda: self.functionsbtn("-"))
        self.calc.btn_multiplicar.clicked.connect(lambda: self.functionsbtn("*"))
        self.calc.btn_dividir.clicked.connect(lambda: self.functionsbtn("/"))
        self.calc.btn_PA.clicked.connect(lambda: self.functionsbtn("("))
        self.calc.btn_PC.clicked.connect(lambda: self.functionsbtn(")"))
        self.calc.btn_point.clicked.connect(lambda: self.functionsbtn("."))
        self.calc.btn_igual.clicked.connect(lambda: self.functionsbtn("="))
        self.calc.btn_borrar.clicked.connect(lambda: self.functionsbtn("C"))
        
    def keyPressEvent(self, event):
        events.getLabel(self.calc.lbl_title)
        events.teclas(event,self.calc.lbl_title, self.calc.edit_pantalla)  
    
    def functionsbtn(self,boton):
        events.getLabel(self.calc.lbl_title)
        texto = self.calc.lbl_title.text()

        if ((boton.isnumeric() == True) or (boton.isalnum()==False) and boton != "="):
            self.calc.lbl_title.setText(texto+boton)
        elif boton == "C":
            self.calc.lbl_title.setText(texto[:-1])
        elif boton == "=":
            if self.calc.edit_pantalla.text() != "":
                self.calc.edit_pantalla.clear()
            try:
                self.calc.edit_pantalla.insert(str(eval(texto)))
                
            except:
                self.calc.edit_pantalla.setText("Error: verifique la operación ingresada")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Calculadora()
    my_app.setWindowIcon(QIcon("Images/calculadora.ico"))
    my_app.show()
    sys.exit(app.exec_())


