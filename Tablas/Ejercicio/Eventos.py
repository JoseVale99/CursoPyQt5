

def enviar_a_view(row,tableWidget, tableView,QStandardItem):
    items = [tableWidget.item(row,column).text() for column in range(tableWidget.columnCount())]
    row = tableView.model().rowCount()
    columna = 0
    for item in items:
        tableView.model().setItem(row, columna, QStandardItem(item))
        columna += 1
    tableView.model().layoutChanged.emit()

def enviar_a_widget(fila, tableWidget, tableView,QTableWidgetItem):
    items = [tableView.model().index(fila, columna).data() for columna in range(tableWidget.columnCount())]
    fila = tableWidget.rowCount()
    columna = 0
    tableWidget.insertRow(fila)
    for item in items:
        tableWidget.setItem(fila, columna, QTableWidgetItem(item))
        columna += 1
