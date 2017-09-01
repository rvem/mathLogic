from parser import parse
from expression import *

axioms = [parse(x) for x in
          ["a->(b->a)",
           "(a->b)->(a->b->c)->(a->c)",
           "a->b->a&b",
           "a&b->a",
           "a&b->b",
           "a->a|b",
           "a->b|a",
           "(a->b)->(c->b)->(a|c->b)",
           "(a->b)->(a->!b)->!a",
           "!!a->a"]
          ]

formal_axioms = [parse(x) for x in
                 ["a=b->a'=b'",
                  "a=b->a=c->b=c",
                  "a'=b'->a=b",
                  "!(a'=0)",
                  "a+b'=(a+b)'",
                  "a+0=a",
                  "a*0=0",
                  "a*b'=a*b+a"
                  ]
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
            if check(expr.left, axiom.left, dictionary):
                return check(expr.right, axiom.right, dictionary)
    else:
        return False


def is_classical_axiom(expr):
    for i in range(len(axioms)):
        if check(expr, axioms[i], dict()):
            return i + 1
    return 0


def get_free(expr, variables, free_variables):
    if type(expr) is Variable:
        if expr not in variables.keys():
            free_variables.add(expr.val)
    elif type(expr) is Predicate:
        for val in expr.val:
            get_free(val, variables, free_variables)
    elif type(expr) is Any or type(expr) is Exists:
        if expr.var not in variables.keys():
            variables[expr.var] = 1
        else:
            variables[expr.var] += 1
        get_free(expr.val, variables, free_variables)
        variables[expr.var] -= 1
        if variables[expr.var] == 0:
            variables.pop(expr.var)
    elif isinstance(expr, Unary):
        return get_free(expr.val, variables, free_variables)
    elif isinstance(expr, Binary):
        return get_free(expr.left, variables, free_variables) & get_free(expr.right, variables,
                                                                         free_variables)
    return free_variables


def get_free_variables(expr):
    s = set()
    get_free(expr, dict(), s)
    return s


def free_subtract(axiom, expr, variable, locked_variables, variables):
    if type(axiom) is Variable:
        if axiom != variable:
            return axiom == expr
        if axiom.val in locked_variables:
            return axiom == expr
        else:
            if axiom not in variables:
                freeVariables = get_free_variables(expr)
                if len(freeVariables.intersection(locked_variables)) != 0:
                    return False
                variables[axiom] = expr
                return True

            else:
                return variables[axiom] == expr
    elif type(axiom) is type(expr):
        if type(axiom) is Any or type(axiom) is Exists:
            if axiom.var.val not in locked_variables:
                locked_variables[axiom.var.val] = 1
            else:
                locked_variables[axiom.var.val] += 1
            res = free_subtract(axiom.val, expr.val, variable, locked_variables, variables)
            locked_variables[axiom.var.val] -= 1
            if locked_variables[axiom.var.val] == 0:
                locked_variables.pop(axiom.var.val)
            return res
        elif type(axiom) is Predicate:
            if len(axiom.val) != len(expr.val):
                return False
            for i in range(len(axiom.val)):
                if not free_subtract(axiom.val[i], expr.val[i], variable, locked_variables, variables):
                    return False
            return True
        elif isinstance(axiom, Unary):
            return free_subtract(axiom.val, expr.val, variable, locked_variables, variables)
        elif isinstance(axiom, Binary):
            return free_subtract(axiom.left, expr.left, variable, locked_variables, variables) \
                   and free_subtract(axiom.right, expr.right, variable, locked_variables, variables)
    return False


def free_to_subtract(axiom, expr, variable):
    return free_subtract(axiom, expr, variable, dict(), dict())


def is_any_axiom(expr):
    if type(expr) is not Implication or type(expr.left) is not Any:
        return False
    return free_to_subtract(expr.left.val, expr.right, expr.left.var)


def is_exists_axiom(expr):
    if type(expr) is not Implication or type(expr.right) is not Exists:
        return False
    return free_to_subtract(expr.right.val, expr.left, expr.right.var)


def check_9(expr):
    return expr.left.right.var.val in get_free_variables(expr.right) \
           and free_to_subtract(expr.right, expr.left.left, Variable(expr.left.right.var)) \
           and free_to_subtract(expr.right, expr.left.right.val.right, Variable(expr.left.right.var)) \
           and expr.right == expr.left.right.val.left


def check_formal(expr, axiom):
    return expr.hash == axiom.hash


def is_formal_axiom(expr):
    for formal_axiom in formal_axioms:
        if check_formal(expr, formal_axiom):
            return True
    return is_any_axiom(expr) or is_exists_axiom(expr) or ((type(expr) is Implication and type(
        expr.left) is Conjunction and type(expr.left.right) is Any and type(
        expr.left.right.val) is Implication) and check_9(expr))
