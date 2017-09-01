from expression import *

s = ''
i = 0


def parse(str):
    global s, i
    s = str
    i = 0
    return parse_impl()


def parse_var_name():
    global s, i
    name = ''
    while i < len(s) and ('a' <= s[i] <= 'z' or '0' <= s[i] <= '9'):
        name += s[i]
        i += 1
    return name


def parse_predicate_name():
    global s, i
    name = ''
    if not ('A' <= s[i] <= 'Z'):
        return ''
    while i < len(s) and ('A' <= s[i] <= 'Z' or '0' <= s[i] <= '9'):
        name += s[i]
        i += 1
    return name


def parse_arguments():
    global s, i
    res = []
    if i >= len(s) or s[i] != '(':
        return res
    i += 1
    res.append(parse_term())
    while i < len(s) and s[i] != ')':
        i += 1
        res.append(parse_term())
    i += 1
    return res


def parse_impl():
    global s, i
    res = parseDisj()
    if i < len(s) and s[i] == '-':
        i += 2
        expr = parse_impl()
        res = Implication(res, expr)
    return res


def parseDisj():
    global s, i
    res = parse_conj()
    while i < len(s) and s[i] == '|':
        i += 1
        curr = parse_conj()
        res = Disjunction(res, curr)
    return res


def parse_conj():
    global s, i
    res = parse_unary()
    while i < len(s) and s[i] == '&':
        i += 1
        curr = parse_unary()
        res = Conjunction(res, curr)
    return res


def parse_unary():
    global s, i
    if s[i] == '?' or s[i] == '@':
        return parse_quant()
    elif s[i] == '!':
        i += 1
        res = parse_unary()
        res = Not(res)
        return res
    elif s[i] == '(':
        i += 1
        tmp = i
        res = parse_impl()
        if res is None:
            i += 1
            return res
        i = tmp - 1
    res = parse_predicate()
    if res is not None:
        return res

    if i < len(s) and s[i] == '(':
        i += 1
        res = parse_impl()
        i += 1
        return res

    name = parse_var_name()
    res = Variable(name)
    return res


def parse_quant():
    global s, i
    c = s[i]
    i += 1
    name = parse_var_name()
    res = parse_unary()
    if res is None:
        return None
    if c == '@':
        return Any(Variable(name), res)
    else:
        return Exists(Variable(name), res)


def parse_predicate():
    global s, i
    name = parse_predicate_name()
    if name == '':
        return parse_eq()
    else:
        args = parse_arguments()
        return Predicate(name, args)


def parse_eq():
    global s, i
    tmp = i
    res = parse_term()
    if i >= len(s) or s[i] != '=':
        i = tmp
        return None
    i += 1
    curr = parse_term()
    res = Equals(res, curr)
    return res


def parse_term():
    global s, i
    res = parse_sum()
    while i < len(s) and s[i] == '+':
        i += 1
        curr = parse_sum()
        res = Sum(res, curr)
    return res


def parse_sum():
    global s, i
    res = parse_mul()
    while i < len(s) and s[i] == '*':
        i += 1
        curr = parse_mul()
        res = Mul(res, curr)
    return res


def parse_mul():
    global s, i
    if i < len(s) and s[i] == '(':
        i += 1
        res = parse_term()
        i += 1
        return parse_next(res)
    name = parse_var_name()
    if i < len(s) and s[i] == '(':
        args = parse_arguments()
        res = Predicate(name, args)
    else:
        res = Variable(name)
    return parse_next(res)


def parse_next(expr):
    global s, i
    while i < len(s) and s[i] == '\'':
        i += 1
        expr = Next(expr)
    return expr
