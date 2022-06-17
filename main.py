# Argument parsing and run function.
import argparse
from exp_parser import *
from grover_operator import *
from phase_estimation import PhaseEstimation
from sat_circuit import *
from simulator import *
import matplotlib.pyplot as plt


def run(input_expr):
    parsed = CNFParser(input_expr)  # convert expression string to CNF form
    grover_op = GroverOperator(parsed.var_count, parsed.cnf_exp)  # create Grover's circuit from CNF
    phase_esti = PhaseEstimation(grover_op)  # find number of solutions using phase estimation
    if phase_esti.M == 0:
        raise SystemExit("No solution found")
    sat_cir = SATCircuit(parsed.var_count, parsed.cnf_exp, phase_esti.M, grover_op.main_circuit)
    sat_cir.main_circuit.draw('mpl')  # draw circuit
    print(simulateStatevector(sat_cir.main_circuit).draw())  # print statevectors
    simulateQasm(sat_cir.main_circuit)  # simulate and show histogram


if __name__ == '__main__':
    # parse argument and run
    parser = argparse.ArgumentParser(description='solve k-SAT problem using grover\'s algorithm')
    parser.add_argument('expr', metavar='expr', type=str, help='enter boolean expression to solve')
    args = parser.parse_args()
    run(args.expr)
    plt.show()
