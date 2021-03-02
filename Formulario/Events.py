import  re


control = [None for i in range(4)]  #[NONE,NONE,NONE,NONE]

def getValidarText(line_edit):
    if (line_edit.text().isalpha() or " " in line_edit.text()):
        line_edit.setStyleSheet("border: 1px solid green;")
        control[0] = True
    else:
        line_edit.setStyleSheet("border: 1px solid red;")
        control[0] = False

def getValidarNum(line_edit):
    if (re.search("(?<=[a-zA-Z])", line_edit.text()) is None) and (re.search("[+*]|[-*]|[0-9]", line_edit.text()) is not None):
        line_edit.setStyleSheet("border: 1px solid green;")
        control[1] = True
    else:
        line_edit.setStyleSheet("border: 1px solid red;")
        control[1] = False

def getDirecccion(line_edit):
    if line_edit.text().isalnum() or " " in line_edit.text():
        line_edit.setStyleSheet("border: 1px solid green;")
        control[2] = True
    else:
        line_edit.setStyleSheet("border: 1px solid red;")
        control[2] = False

def getValidarEdad(spin):
    if spin.value() <18:
        spin.setStyleSheet("border: 1px solid red;")
        control[3] = False
    else:
        spin.setStyleSheet("border: 1px solid green;")
        control[3] = True

def getValidarRegistro(objectos):
    if control.count(True) == 4:
        objectos[5].resultado = 1
    else:
        objectos[5].resultado = 2
