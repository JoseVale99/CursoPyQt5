from PyQt5.QtWidgets import (QLabel,QPushButton,QScrollBar,QHBoxLayout,
QGridLayout,QFrame,QSizePolicy, QWidget,QSpacerItem,QTableWidget,QTableWidgetItem)
from PyQt5.QtCore import QSize, Qt,QCoreApplication, QMetaObject
from  PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 520)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setMaximumSize(QSize(420, 600))
        MainWindow.setStyleSheet("")
        self.Ventana = QWidget(MainWindow)
        self.Ventana.setMaximumSize(QSize(500, 600))
        self.Ventana.setStyleSheet("*{\n"
"    font-family:  century gothic;\n"
"\n"
"}\n"
"QSizeGrip{\n"
"background:transparent;\n"
"}\n"
"\n"
"QWidget#Ventana{\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel{\n"
"    color:white;\n"
"}\n"
"\n"
"")
        self.Ventana.setObjectName("Ventana")
        self.horizontalLayout = QHBoxLayout(self.Ventana)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.VentanaFrame = QFrame(self.Ventana)
        self.VentanaFrame.setStyleSheet("QFrame#VentanaFrame{\n"
" background-color: qlineargradient(spread:pad, x1:0.953, y1:1, x2:1, y2:0, stop:0 #075E54, stop:1 #128C7E); \n"
"    border-radius:5px;\n"
"}\n"
"")
        self.VentanaFrame.setFrameShape(QFrame.StyledPanel)
        self.VentanaFrame.setFrameShadow(QFrame.Raised)
        self.VentanaFrame.setObjectName("VentanaFrame")
        self.gridLayout_2 = QGridLayout(self.VentanaFrame)
        self.gridLayout_2.setContentsMargins(10, 15, 15, 5)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Contenedor =  QFrame(self.VentanaFrame)
        self.Contenedor.setStyleSheet("QFrame#Contenedor{\n"
"     background-color: #128c7e;\n"
"        border-radius:20px;\n"
"}")
        self.Contenedor.setFrameShape(QFrame.StyledPanel)
        self.Contenedor.setFrameShadow(QFrame.Raised)
        self.Contenedor.setObjectName("Contenedor")
        self.gridLayout = QGridLayout(self.Contenedor)
        self.gridLayout.setObjectName("gridLayout")
        self.frameAcciones = QFrame(self.Contenedor)
        sizePolicy =QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameAcciones.sizePolicy().hasHeightForWidth())
        self.frameAcciones.setSizePolicy(sizePolicy)
        self.frameAcciones.setStyleSheet("QFrame#frameAcciones{\n"
"    border:none;\n"
"}\n"
"QPushButton#btn_abrir{\n"
"    background-color: #ECF0F1;\n"
"    border-radius: 5px;\n"
"    color: #000;\n"
"}\n"
"\n"
"QPushButton#btn_abrir:hover{\n"
"    background-color: #BDC3C7;\n"
"    color: #000;\n"
"}")
        self.frameAcciones.setFrameShape(QFrame.StyledPanel)
        self.frameAcciones.setFrameShadow(QFrame.Raised)
        self.frameAcciones.setObjectName("frameAcciones")
        self.gridLayout_4 = QGridLayout(self.frameAcciones)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_exportar = QPushButton(self.frameAcciones)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exportar.sizePolicy().hasHeightForWidth())
        self.btn_exportar.setSizePolicy(sizePolicy)
        self.btn_exportar.setMinimumSize(QSize(100, 30))
        self.btn_exportar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportar.setStyleSheet("QPushButton#btn_exportar{\n"
"    background-color: #ECF0F1;\n"
"    border-radius: 5px;\n"
"    color: #000;\n"
"}\n"
"\n"
"QPushButton#btn_exportar:hover{\n"
"    background-color: #BDC3C7;\n"
"    color: #000;\n"
"}")
        icon = QIcon()
        icon.addPixmap(QPixmap("Images/exportar.png"), QIcon.Normal, QIcon.Off)
        self.btn_exportar.setIcon(icon)
        self.btn_exportar.setObjectName("btn_exportar")
        self.gridLayout_4.addWidget(self.btn_exportar, 0, 2, 1, 1)
        self.btn_abrir = QPushButton(self.frameAcciones)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_abrir.sizePolicy().hasHeightForWidth())
        self.btn_abrir.setSizePolicy(sizePolicy)
        self.btn_abrir.setMinimumSize(QSize(100, 30))
        self.btn_abrir.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("Images/anadir.png"), QIcon.Normal, QIcon.Off)
        self.btn_abrir.setIcon(icon1)
        self.btn_abrir.setObjectName("btn_abrir")
        self.gridLayout_4.addWidget(self.btn_abrir, 0, 1, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.frameAcciones, 2, 0, 1, 1)
        self.header = QFrame(self.Contenedor)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setStyleSheet("QFrame{\n"
" border: none;\n"
"}")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.header.setObjectName("header")
        self.boxFlags = QHBoxLayout(self.header)
        self.boxFlags.setContentsMargins(5, 0, 0, 5)
        self.boxFlags.setSpacing(5)
        self.boxFlags.setObjectName("boxFlags")
        self.btn_rojo = QPushButton(self.header)
        self.btn_rojo.setMaximumSize(QSize(16, 16))
        self.btn_rojo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rojo.setStyleSheet("QPushButton#btn_rojo{\n"
"border-radius: 8px;\n"
"background-color: red;\n"
"}\n"
"QPushButton#btn_rojo:hover{\n"
"border-radius: 8px;\n"
"background-color: #b60600;\n"
"}")
        self.btn_rojo.setText("")
        self.btn_rojo.setObjectName("btn_rojo")
        self.boxFlags.addWidget(self.btn_rojo)
        self.btn_verde = QPushButton(self.header)
        self.btn_verde.setMaximumSize(QSize(16, 16))
        self.btn_verde.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_verde.setStyleSheet("QPushButton#btn_verde{\n"
"border-radius: 8px;\n"
"background-color: #27ae60;\n"
"}\n"
"QPushButton#btn_verde:hover{\n"
"border-radius: 8px;\n"
"background-color: #7efc00;\n"
"}")
        self.btn_verde.setText("")
        self.btn_verde.setObjectName("btn_verde")
        self.boxFlags.addWidget(self.btn_verde)
        self.btn_amarillo = QPushButton(self.header)
        self.btn_amarillo.setMaximumSize(QSize(16, 16))
        self.btn_amarillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_amarillo.setStyleSheet("QPushButton#btn_amarillo{\n"
"border-radius: 8px;\n"
"background-color: yellow;\n"
"}\n"
"QPushButton#btn_amarillo:hover{\n"
"border-radius: 8px;\n"
"background-color: #f1c40f;\n"
"}")
        self.btn_amarillo.setText("")
        self.btn_amarillo.setObjectName("btn_amarillo")
        self.boxFlags.addWidget(self.btn_amarillo)
        spacerItem2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.boxFlags.addItem(spacerItem2)
        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)
        self.frameLogo = QFrame(self.Contenedor)
        self.frameLogo.setStyleSheet("QFrame#frameLogo{\n"
"    border:none;\n"
"}\n"
"")
        self.frameLogo.setFrameShape(QFrame.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Raised)
        self.frameLogo.setObjectName("frameLogo")
        self.gridLayout_3 = QGridLayout(self.frameLogo)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.icon = QLabel(self.frameLogo)
        self.icon.setStyleSheet("")
        self.icon.setText("")
        self.icon.setPixmap(QPixmap("Images/whatsapp.png"))
        self.icon.setAlignment(Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.gridLayout_3.addWidget(self.icon, 0, 0, 1, 1)
        self.lblText = QLabel(self.frameLogo)
        font = QFont()
        font.setFamily("century gothic")
        font.setBold(True)
        font.setWeight(75)
        self.lblText.setFont(font)
        self.lblText.setStyleSheet("")
        self.lblText.setAlignment(Qt.AlignCenter)
        self.lblText.setObjectName("lblText")
        self.gridLayout_3.addWidget(self.lblText, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frameLogo, 1, 0, 1, 1)
        self.label = QLabel(self.Contenedor)
        font = QFont()
        font.setFamily("century gothic")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.frame_tabla = QFrame(self.Contenedor)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_tabla.sizePolicy().hasHeightForWidth())
        self.frame_tabla.setSizePolicy(sizePolicy)
        self.frame_tabla.setStyleSheet("QFrame#frame_tabla{\n"
"    border:none;\n"
"}")
        self.frame_tabla.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla.setFrameShadow(QFrame.Raised)
        self.frame_tabla.setObjectName("frame_tabla")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tabla)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.tabla = QTableWidget(self.frame_tabla)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla.sizePolicy().hasHeightForWidth())
        self.tabla.setSizePolicy(sizePolicy)
        self.tabla.setMinimumSize(QSize(250, 0))
        self.tabla.setStyleSheet("*{\n"
"color: #000;\n"
"}\n"
"QTableWidget#tabla:item{\n"
"    color: blue;\n"
"    font-family: bold;\n"
"}\n"
"\n"
"QTableWidget#tabla{\n"
"    border-radius:4px;\n"
"    background-color: #128c7e;\n"
"}\n"
"QScrollBar:vertical{\n"
"    border: 1px solid #999999;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"    min-height: 0px;\n"
"    border: 0px solid red;\n"
"    border-radius: 4px;\n"
"    background-color: #3a727f;\n"
"}    \n"
"QScrollBar::add-line:vertical{\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"    height:0px;\n"
"    subcontrol-position:top;\n"
"    sucontrol-origin:margin;\n"
"}\n"
"QTableWidget:item:selected{\n"
"background : #08a785;\n"
"}\n"
"QTableCornerButton:section{\n"
"background-color: #00aa7f;\n"
"}\n"
"QHeaderView:section{\n"
"background-color: #00aa7f;\n"
"}\n"
"\n"
"")
        self.tabla.setRowCount(10)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(2)
        item = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.tabla)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addWidget(self.frame_tabla, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.Contenedor, 0, 1, 1, 1)
        self.Grip = QLabel(self.VentanaFrame)
        self.Grip.setMaximumSize(QSize(10, 10))
        self.Grip.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.Grip.setLayoutDirection(Qt.RightToLeft)
        self.Grip.setStyleSheet("QLabel#Grip:hover{\n"
"    background: rgb(18,140,126);\n"
"    border-radius:5px;\n"
"}\n"
"QLabel#Grip{\n"
" background-color: qlineargradient(spread:pad, x1:0.953, y1:1, x2:1, y2:0, stop:0 #075E54, stop:1 #128C7E); \n"
"    border-radius:5px;\n"
"}")
        self.Grip.setText("")
        self.Grip.setObjectName("Grip")
        self.gridLayout_2.addWidget(self.Grip, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.VentanaFrame)
        MainWindow.setCentralWidget(self.Ventana)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_exportar.setText(_translate("MainWindow", "Exportar"))
        self.btn_abrir.setText(_translate("MainWindow", "Abrir TXT"))
        self.lblText.setText(_translate("MainWindow", "WhatsPy"))
        self.label.setText(_translate("MainWindow", "Todavia no haz cargado ningun chat"))
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Numeros"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mensajes"))
