from pysat.solvers import Glucose3


class LatinSquareSolver():
    __result = []
    __size = 0
    __combination = []

    def solve(self, size):
        self.size = size
        solver = Glucose3()
        self.build_cnf(solver)

        if solver.solve():
            self.build_matrix(solver.get_model())
        else:
            print("Not Satisfiable")

    def build_cnf(self, solver):
        # Rule 1
        cnf = []
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                for x in range(1, self.size+1):
                    cnf.append(self.convert(i, j, x))
                solver.add_clause(cnf)
                cnf = []

        # Rule 2
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                for x in range(1, self.size):
                    for y in range(x+1, self.size+1):
                        solver.add_clause(
                            [-(self.convert(i, j, x)), -(self.convert(i, j, y))]
                        )

        # Rule 3
        for i in range(1, self.size+1):
            for x in range(1, self.size+1):
                for j in range(1, self.size+1):
                    cnf.append(self.convert(i, j, x))
                solver.add_clause(cnf)
                cnf = []

        # Rule 4
        for j in range(1, self.size+1):
            for x in range(1, self.size+1):
                for i in range(1, self.size+1):
                    cnf.append(self.convert(i, j, x))
                solver.add_clause(cnf)
                cnf = []

    def build_matrix(self, model):
        for i in range(self.size):
            self.__result.append([])
        for element in model:
            if element > 0:
                clause = self.__combination[element-1]
                self.__result[clause[0]].insert(clause[1], clause[2])

    def convert(self, i, j, k):
        row = (i-1)*(self.size * self.size)
        col = (j-1)*self.size
        value = k-1
        index = row + col + value + 1

        if [i-1, j-1, k] not in self.__combination:
            self.__combination.insert(index, [i-1, j-1, k])
        return index

    def get_result(self):
        return self.__result
