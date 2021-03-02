def Abir_archivo(file_dialog, textEdit,editor):
    ruta = file_dialog.getOpenFileName(None,"Seleecione un archivo","","Python (*.py);;Texto (*.txt)")
    if ruta[0] != "":
        with open(ruta[0],"r", encoding="utf-8") as archivo:
            textEdit.setText(("").join(archivo.readlines()))
    editor.setWindowTitle(f"Editor de texto - {ruta[0]}")
    return ruta[0]



def GuardarComo(file_dialog,textEdit,editor):
    ruta = file_dialog.getSaveFileName(None,"Guardar archivo como","","Python (*.py);;Texto (*.txt)")
    if ruta[0] != "":
        with open(ruta[0],"w",encoding="utf-8") as archivo:
            archivo.write(textEdit.toPlainText())
    editor.setWindowTitle(f"Editor de texto - {ruta[0]}")
    return ruta[0]