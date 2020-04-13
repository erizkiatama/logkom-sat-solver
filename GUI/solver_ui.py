from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Solver(object):
    def setupUi(self, Solver, n):
        Solver.setObjectName("Solver")
        Solver.resize((30*n)+42, (30*n)+112)
        Solver.setMinimumSize(QtCore.QSize((30*6)+42, (30*6)+112))
        Solver.setMaximumSize(QtCore.QSize((30*n)+42, (30*n)+112))
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Solver)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QtWidgets.QLabel(Solver)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QtWidgets.QTableWidget(Solver)
        self.tableWidget.setRowCount(n)
        self.tableWidget.setColumnCount(n)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.back_button = QtWidgets.QPushButton(Solver)
        self.back_button.setObjectName("back_button")
        
        self.horizontalLayout.addWidget(self.back_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Solver)
        QtCore.QMetaObject.connectSlotsByName(Solver)

    def retranslateUi(self, Solver):
        _translate = QtCore.QCoreApplication.translate
        Solver.setWindowTitle(_translate("Solver", "Solver"))
        self.label.setText(_translate("Solver", "Hit \'Solve\' to show solution."))
        self.back_button.setText(_translate("Solver", "Back"))
