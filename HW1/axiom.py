from parser import parse
from expression import *

axioms = [parse(x) for x in
          ["A->(B->A)",
           "(A->B)->(A->B->C)->(A->C)",
           "A->B->A&B",
           "A&B->A",
           "A&B->B",
           "A->A|B",
           "A->B|A",
           "(A->B)->(C->B)->(A|C->B)",
           "(A->B)->(A->!B)->!A",
           "!!A->A"]
          ]


def check(expr, axiom, dictionary):
    if type(axiom) is Variable:
        if axiom in dictionary:
            return dictionary[axiom] == expr
        else:
            dictionary[axiom] = expr
            return True
    elif type(expr) is type(axiom):
        if isinstance(axiom, Unary):
            return check(expr.val, axiom.val, dictionary)
        else:
            left = check(expr.left, axiom.left, dictionary)
            if left:
                return check(expr.right, axiom.right, dictionary)
    else:
        return False


def isAxiom(expr):
    for i in range(len(axioms)):
        if check(expr, axioms[i], {}):
            return i + 1
    return 0
