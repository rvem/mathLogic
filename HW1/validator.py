from parser import parse
from expression import *
from axiom import isAxiom


def main():
    fin = open("test.in", "r")
    fout = open("test.out", "w")

    firstLine = fin.readline()
    if firstLine.find("|-") != -1:
        assumptionsList = firstLine.split("|-")[0].split()
    else:
        assumptionsList = []
    assumptions = {}
    expressions = set()
    for i in range(len(assumptionsList)):
        assumptions[assumptionsList[i]] = i + 1
    proof = [parse(x) for x in fin.readlines()]
    i = 1
    for expr in proof:
        proved = False
        if len(assumptionsList) > 0:
            if expr in assumptions:
                proved = True
                print(i, expr, "Предполож.", assumptions[expr], file=fout)
        if not proved:
            a = isAxiom(expr)
            if a != 0:
                proved = True
                print(i, expr, "Сх. Аксиомы", a, file=fout)
        if not proved:
            for j in range(i - 1, -1, -1):
                mp = Implication(proof[j], expr)
                if mp in expressions:
                    print(i, expr, "M.P.", j + 1, expressions[mp], file=fout)
                    proved = True
        if proved:
            expressions.add(expr)
        if not proved:
            print(i, expr, "Не доказано", file=fout)
        i += 1
    fin.close()
    fout.close()


main()
