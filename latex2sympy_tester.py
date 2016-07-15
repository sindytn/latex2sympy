__author__ = 'sindytan'

import sympy
from process_latex import process_sympy
from sympy.core import Atom
from sympy.core import Function
from sympy.core import Derivative
from sympy.printing.dot import dotprint
from sympy import *

# myExpr = "f_{X+Y}(a) = \\frac{d}{da}\int_{\\infty}^{\\infty} F_X(a-y)f_Y(y)dy"
# myExpr = "f_{X+Y}(a) = \\frac{d}{da}\int_{\\infty}^{\\infty} F_X(a-y)f_Y(y)dy + N"
myExpr = '-2 (\\sum_i y_i˙- n w_0) '
# myExpr = '-2 (\sum_i y_i - (\sum_i x_i^T)  w˙- n w_0)'
expr = process_sympy(myExpr)
print expr

# get list of all subtrees / arguments of a SymPy expression
def get_subtrees(expr, subtrees):
    if len(expr.args) > 0:
        if expr.func not in subtrees:
            subtrees += [expr.func]
        for arg in expr.args:
            # if (not isinstance(arg, Atom)) and (arg not in subtrees):
            if arg not in subtrees:
                subtrees += [arg]
            get_subtrees(arg, subtrees)
        return subtrees
    else:
        return subtrees

subtrees = get_subtrees(expr, [])
for st in subtrees:
    print st
