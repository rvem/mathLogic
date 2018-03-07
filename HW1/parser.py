from expression import *

s = ''
i = 0

def parse(str):
    global s, i
    s = str
    i = 0
    return parseImpl()


def parseImpl():
    global s, i
    res = parseDisj()
    while i < len(s) and s[i] == '-':
        i += 2
        expr = parseImpl()
        if expr is None:
            return None
        res = Implication(res, expr)
    return res


def parseDisj():
    global s, i
    res = parseConj()
    while i < len(s) and s[i] == '|':
        i += 1
        curr = parseConj()
        res = Disjunction(res, curr)
    return res


def parseConj():
    global s, i
    res = parseNot()
    while i < len(s) and s[i] == '&':
        i += 1
        curr = parseNot()
        res = Conjunction(res, curr)
    return res

def parseNot():
    global s, i
    if s[i] == "!":
        i += 1
        res = parseNot()
        return Not(res)
    elif s[i] == '(':
        i += 1
        res = parseImpl()
        i += 1
        return res
    else:
        name = ''
        while i < len(s) and ('A' <= s[i] <= 'Z' or '0' <= s[i] <= '9'):
            name += s[i]
            i += 1
        return Variable(name)