from solver import LatinSquareSolver

n = input("Please enter your desired size: ")

solver = LatinSquareSolver()
solver.solve(int(n))
print(solver.get_result())
