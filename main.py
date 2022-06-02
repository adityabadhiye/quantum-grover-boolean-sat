# Argument parsing and run function.
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
    if phase_esti.M == 0:
        raise SystemExit("No solution found")
    sat_cir = SATCircuit(parsed.var_count, parsed.cnf_exp, phase_esti.M, grover_op.main_circuit)
    sat_cir.main_circuit.draw('mpl')
    simulateStatevector(sat_cir.main_circuit)
    simulateQasm(sat_cir.main_circuit)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='solve k-SAT problem using grover\'s algorithm')
    parser.add_argument('expr', metavar='expr', type=str, help='enter boolean expression to solve')
    args = parser.parse_args()
    run(args.expr)
    plt.show()
