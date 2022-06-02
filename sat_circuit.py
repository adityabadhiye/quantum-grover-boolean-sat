from qiskit import QuantumCircuit
from math import pi, sqrt, acos


class SATCircuit:
    def __init__(self, n, cnf, M, grover_operator):
        eq = len(cnf)
        total = n + eq + 1

        circuit = QuantumCircuit(total, n)
        circuit.h(range(n))
        circuit.h(total - 1)
        circuit.z(total - 1)

        itr = round(((pi / (2 * acos(sqrt((pow(2, n) - M) / pow(2, n))))) - 1) / 2)
        if itr == 0:
            raise SystemExit("No solution found")
        for x in range(itr):
            circuit = circuit.compose(grover_operator)

        circuit.measure(range(n), range(n))
        self.main_circuit = circuit
