from solver import LatinSquareSolver

n = input("Please enter your desired size: ")

solver = LatinSquareSolver()
solver.solve(int(n))

for row in solver.get_result():
    print(row)
