# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registro.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 279)
        MainWindow.setMinimumSize(QtCore.QSize(250, 0))
        MainWindow.setMaximumSize(QtCore.QSize(500, 279))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_tel = QtWidgets.QLabel(self.frame)
        self.lbl_tel.setObjectName("lbl_tel")
        self.gridLayout_2.addWidget(self.lbl_tel, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.lbl_ap = QtWidgets.QLabel(self.frame)
        self.lbl_ap.setObjectName("lbl_ap")
        self.gridLayout_2.addWidget(self.lbl_ap, 1, 0, 1, 1)
        self.Edit_dir = QtWidgets.QLineEdit(self.frame)
        self.Edit_dir.setMaxLength(120)
        self.Edit_dir.setClearButtonEnabled(True)
        self.Edit_dir.setObjectName("Edit_dir")
        self.gridLayout_2.addWidget(self.Edit_dir, 2, 1, 1, 1)
        self.Edit_tel = QtWidgets.QLineEdit(self.frame)
        self.Edit_tel.setMaxLength(30)
        self.Edit_tel.setClearButtonEnabled(True)
        self.Edit_tel.setObjectName("Edit_tel")
        self.gridLayout_2.addWidget(self.Edit_tel, 3, 1, 1, 1)
        self.lbl_dir = QtWidgets.QLabel(self.frame)
        self.lbl_dir.setObjectName("lbl_dir")
        self.gridLayout_2.addWidget(self.lbl_dir, 2, 0, 1, 1)
        self.Edit_name = QtWidgets.QLineEdit(self.frame)
        self.Edit_name.setMaxLength(40)
        self.Edit_name.setFrame(True)
        self.Edit_name.setClearButtonEnabled(True)
        self.Edit_name.setObjectName("Edit_name")
        self.gridLayout_2.addWidget(self.Edit_name, 0, 1, 1, 1)
        self.Edit_ap = QtWidgets.QLineEdit(self.frame)
        self.Edit_ap.setMaxLength(50)
        self.Edit_ap.setClearButtonEnabled(True)
        self.Edit_ap.setObjectName("Edit_ap")
        self.gridLayout_2.addWidget(self.Edit_ap, 1, 1, 1, 1)
        self.lbl_name = QtWidgets.QLabel(self.frame)
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout_2.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.btn_reg = QtWidgets.QPushButton(self.frame)
        self.btn_reg.setObjectName("btn_reg")
        self.gridLayout_2.addWidget(self.btn_reg, 5, 1, 1, 1)
        self.box_edad = QtWidgets.QSpinBox(self.frame)
        self.box_edad.setMinimum(17)
        self.box_edad.setMaximum(100)
        self.box_edad.setObjectName("box_edad")
        self.gridLayout_2.addWidget(self.box_edad, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registro"))
        self.groupBox.setTitle(_translate("MainWindow", "Formularrio de Registro"))
        self.lbl_tel.setText(_translate("MainWindow", "Edad"))
        self.label_3.setText(_translate("MainWindow", "Telefono"))
        self.lbl_ap.setText(_translate("MainWindow", "Apeellidos"))
        self.Edit_dir.setPlaceholderText(_translate("MainWindow", "Ingresa tu Dirección"))
        self.Edit_tel.setPlaceholderText(_translate("MainWindow", "Ingresa tu número de telefono"))
        self.lbl_dir.setText(_translate("MainWindow", "Dirrecion"))
        self.Edit_name.setPlaceholderText(_translate("MainWindow", "Ingresa tu nombre"))
        self.Edit_ap.setPlaceholderText(_translate("MainWindow", "Ingresa tu apellido"))
        self.lbl_name.setText(_translate("MainWindow", "Nombre"))
        self.btn_reg.setText(_translate("MainWindow", "Registrarse"))
        self.box_edad.setSpecialValueText(_translate("MainWindow", "(Ingresa tu edad mayores de 18)"))


