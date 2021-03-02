from PyQt5.QtWidgets import (QApplication,
    QMainWindow,QMessageBox, QDesktopWidget)
import  sys
from  Vista.Vista import  Ui_MainWindow
from  random import randint
from Desing.Style import style

class  Game(QMainWindow):
    def __init__(self):
        super(Game,self).__init__()
        self.game = Ui_MainWindow()
        self.game.setupUi(self)
        self.setStyleSheet(style)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), 
        int((screen.height() - size.height())/2)) 
        
        self.contador = 0
        self.jugador = randint(1,2)
        self.buttons = [self.game.btn_1,self.game.btn_2,self.game.btn_3,
        self.game.btn_4,self.game.btn_5,self.game.btn_6,
        self.game.btn_7,self.game.btn_8,self.game.btn_9
        ]
        self.game.btn_1.clicked.connect(lambda: self.btnClicked(self.game.btn_1))
        self.game.btn_2.clicked.connect(lambda: self.btnClicked(self.game.btn_2))
        self.game.btn_3.clicked.connect(lambda: self.btnClicked(self.game.btn_3))
        self.game.btn_4.clicked.connect(lambda: self.btnClicked(self.game.btn_4))
        self.game.btn_5.clicked.connect(lambda: self.btnClicked(self.game.btn_5))
        self.game.btn_6.clicked.connect(lambda: self.btnClicked(self.game.btn_6))
        self.game.btn_7.clicked.connect(lambda: self.btnClicked(self.game.btn_7))
        self.game.btn_8.clicked.connect(lambda: self.btnClicked(self.game.btn_8))
        self.game.btn_9.clicked.connect(lambda: self.btnClicked(self.game.btn_9))
        self.game.btn_reiniciar.clicked.connect(self.reiniciar)
    
    def btnClicked(self,boton):
        if self.jugador == 1:
            boton.setText("X")
            boton.setStyleSheet("color:#fff;\
             background: #2A58B3;")
            self.jugador = 2
        else:
            boton.setText("O")
            boton.setStyleSheet("color: #000;\
            background: #FF9515;")
            self.jugador = 1
        boton.setEnabled(False)
        self.contador += 1
        self.control()
        


    def control(self):
        #  Filas  & Columnas  
        if((self.game.btn_1.text() == "X" and self.game.btn_2.text() == "X" and self.game.btn_3.text() == "X") 
        or (self.game.btn_4.text() == "X" and self.game.btn_5.text() == "X" and self.game.btn_6.text() == "X") 
        or (self.game.btn_7.text() == "X" and self.game.btn_8.text() == "X" and self.game.btn_9.text() == "X") 
        or (self.game.btn_1.text() == "X" and self.game.btn_4.text() == "X" and self.game.btn_7.text() == "X") 
        or (self.game.btn_2.text() == "X" and self.game.btn_5.text() == "X" and self.game.btn_8.text() == "X") 
        or (self.game.btn_3.text() == "X" and self.game.btn_6.text() == "X" and self.game.btn_9.text() == "X") 
        or (self.game.btn_1.text() == "X" and self.game.btn_5.text() == "X" and self.game.btn_9.text() == "X") 
        or (self.game.btn_3.text() == "X" and self.game.btn_5.text() == "X" and self.game.btn_7.text() == "X")):
            self.ganador(1,"X") 
        
        elif((self.game.btn_1.text() == "O" and self.game.btn_2.text() == "O" and self.game.btn_3.text() == "O") 
        or (self.game.btn_4.text() == "O" and self.game.btn_5.text() == "O" and self.game.btn_6.text() == "O") 
        or (self.game.btn_7.text() == "O" and self.game.btn_8.text() == "O" and self.game.btn_9.text() == "O") 
        or (self.game.btn_1.text() == "O" and self.game.btn_4.text() == "O" and self.game.btn_7.text() == "O") 
        or (self.game.btn_2.text() == "O" and self.game.btn_5.text() == "O" and self.game.btn_8.text() == "O") 
        or (self.game.btn_3.text() == "O" and self.game.btn_6.text() == "O" and self.game.btn_9.text() == "O") 
        or (self.game.btn_1.text() == "O" and self.game.btn_5.text() == "O" and self.game.btn_9.text() == "O") 
        or (self.game.btn_3.text() == "O" and self.game.btn_5.text() == "O" and self.game.btn_7.text() == "O")):
            self.ganador(2,"0")
        
        elif self.contador == 9:
            self.ganador(3)

    def ganador(self, ganador, character=None): 
        msgbox = QMessageBox()
        if 1 <= ganador <= 2:
            msgbox.setWindowTitle("¡Ganador!") 
            msgbox.setText(f"El ganador es el jugador: {ganador} Caracter: {character}")
            for botones in self.buttons:
                botones.setEnabled(False)
            self.contador = 0
        else:
            msgbox.setWindowTitle("Empate") 
            msgbox.setText("Ninguno ganó la ronda") 
        msgbox.exec_() 


    def reiniciar(self):
        for botones in self.buttons:
            botones.setEnabled(True)
            botones.setText("")
            botones.setStyleSheet("background: #000;")
        self.contador = 0
        self.jugador = randint(0,1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Game()
    my_app.show()
    sys.exit(app.exec_())


