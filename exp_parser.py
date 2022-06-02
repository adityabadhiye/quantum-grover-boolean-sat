import re
from sympy.parsing.sympy_parser import parse_expr
from sympy.logic import simplify_logic


class CNFParser:
    def __init__(self, raw_exp):
        self.raw_exp = raw_exp
        self.raw_exp = re.sub('(?i)' + re.escape(' and '), ' & ', self.raw_exp)
        self.raw_exp = re.sub('(?i)' + re.escape(' xor '), ' ^ ', self.raw_exp)
        self.raw_exp = re.sub('(?i)' + re.escape(' or '), ' | ', self.raw_exp)
        self.raw_exp = re.sub('(?i)' + re.escape('not '), '~', self.raw_exp)

        self.exp = parse_expr(self.raw_exp)
        self.var_count = len(self.exp.binary_symbols)
        self.int_to_var = [""] + sorted([str(x) for x in self.exp.binary_symbols])
        self.var_to_int = dict(zip(self.int_to_var[1:], range(1, self.var_count + 1)))

        self.cnf_exp = str(simplify_logic(self.exp, 'cnf'))
        self.cnf_exp = re.sub(r'\(', '', self.cnf_exp)
        self.cnf_exp = re.sub(r'\)', '', self.cnf_exp)
        self.cnf_exp = self.cnf_exp.split(' & ')
        self.cnf_exp = [a.split(' | ') for a in self.cnf_exp]

        for a in self.cnf_exp:
            for i, b in enumerate(a):
                if b[0] != '~':
                    a[i] = self.var_to_int[b]
                else:
                    a[i] = -1 * self.var_to_int[b[1:]]
                    