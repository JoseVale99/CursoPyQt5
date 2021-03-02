from  PyQt5.QtWidgets import *
from first_app import Ui_Form
import  sys

class Counter(QDialog):
    def __init__(self):
        super(Counter,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self) 
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), 
        int((screen.height() - size.height())/2)) 
        self.counter_var = 0
        self.ui.button_click.clicked.connect(self.counter_clicks)


    def counter_clicks(self):
        self.counter_var +=1
        self.ui.counter.setText(str(self.counter_var))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Counter()
    my_app.show()
    sys.exit(app.exec_())