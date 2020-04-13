from PyQt5 import QtCore, QtGui, QtWidgets#, QLineEdit

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(275, 111)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Menu)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QtWidgets.QLabel(Menu)
        self.label.setEnabled(True)
        
        self.label_2 = QtWidgets.QLabel(Menu)
        self.label_2.setEnabled(True)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        
        font_2 = QtGui.QFont()
        font_2.setPointSize(18)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label_2.setFont(font_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.label_2)
        
        self.textbox = QtWidgets.QLineEdit(Menu)
        self.textbox.setObjectName("line_edit")
        self.verticalLayout.addWidget(self.textbox)
        
        self.enter_button = QtWidgets.QPushButton(Menu)
        self.enter_button.setObjectName("enter_button")
        self.verticalLayout.addWidget(self.enter_button)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Latin Square Problem Simulator"))
        self.label.setText(_translate("Menu", "Latin Square Problem Simulator"))
        self.label_2.setText(_translate("Menu", "Input your matrix size"))
        self.enter_button.setText(_translate("Menu", "Enter"))

