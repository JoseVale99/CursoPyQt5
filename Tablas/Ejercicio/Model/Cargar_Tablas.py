from .connection import DataBase

bd = DataBase()

def CargarTablaWidget(tabla, QTableWidgetItem):
    global bd
    data = bd.getData()
    tabla.setColumnCount(len(data[0]))
    tabla.setRowCount(len(data))
    for row in range(len(data)):
        for column in range(len(data[row])):
            tabla.setItem(
            row, column, QTableWidgetItem(str(data[row][column])))

def Cargar_TablaView(tabla,QStandardItemModel,QStandardItem):
    encabezados = ["ID","NOMBRE","APELLIDO","DNI"]
    global bd
    data = bd.getData()
    rows = len(data)
    columns = len(data[0])
    model = QStandardItemModel(rows,columns)
    model.setHorizontalHeaderLabels(encabezados)
    for row in range(len(data)):
        for column in range(columns):
            model.setItem(row,column, QStandardItem(str(data[row][column])))
    tabla.setModel(model)
