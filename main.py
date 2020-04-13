import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from GUI.menu_ui import Ui_Menu
from GUI.solver_ui import Ui_Solver
from solver import LatinSquareSolver

class Menu(QDialog, Ui_Menu):
	def __init__(self, parent=None):
		super(Menu, self).__init__(parent)
		self.setupUi(self)
		self.solverBE = LatinSquareSolver()
		self.enter_button.clicked.connect(self.openSolver)
		self.n = 0

	def openSolver(self):
		self.n = int(self.textbox.text())
		self.solverBE.solve(self.n)
		self.solver = Solver(self.n, self.solverBE, self)
		self.solver.show()

class Solver(QDialog, Ui_Solver):
    def __init__(self, n, solverBE, parent=None):
        super(Solver, self).__init__(parent)
        self.setupUi(self, n)
        self.solve(n, solverBE.get_result())

    def solve(self, n, result):
    	for i in range(n):
    		for j in range(n):
    			item = QTableWidgetItem(str(result[i][j]))
    			item.setFlags(QtCore.Qt.ItemIsEnabled)
    			self.tableWidget.setItem(i, j, item)

def main():
	app = QApplication(sys.argv)
	form = Menu()
	form.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()