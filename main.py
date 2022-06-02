# Argument parsing and run function.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
from exp_parser import *
from grover_operator import *
from phase_estimation import PhaseEstimation
from sat_circuit import *
from simulator import *
import matplotlib.pyplot as plt


def run(input_expr):
    parsed = CNFParser(input_expr)
    grover_op = GroverOperator(parsed.var_count, parsed.cnf_exp)
    phase_esti = PhaseEstimation(grover_op)
    sat_cir = SATCircuit(parsed.var_count, parsed.cnf_exp, phase_esti.M, grover_op.main_circuit)
    simulateStatevector(sat_cir.main_circuit)
    simulateQasm(sat_cir.main_circuit)
    # print(c.circuit)
    # c.circuit.draw('mpl')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='solve k-SAT problem using grover\'s algorithm')
    parser.add_argument('expr', metavar='expr', type=str, help='enter boolean expression to solve')
    args = parser.parse_args()
    # print(args.expr)
    run(args.expr)
    # print(sys.argv[1])
    plt.show()
