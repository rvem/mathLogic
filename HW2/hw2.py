from axiom import *
from sys import argv
from proof_changer import change_proof


def get_assumptions(string):
    assumptions = []
    balance = 0
    assumption = ''
    for i in range(len(string)):
        if string[i] == '(':
            balance += 1
            assumption += string[i]
        elif string[i] == ')':
            balance -= 1
            assumption += string[i]
        elif string[i] == ',' and balance == 0:
            assumptions.append(assumption)
            assumption = ''
        else:
            assumption += string[i]
    return assumption, assumptions


def check_any(cur_type, err, expr, expressions, free_vars, proved):
    if type(expr) is Implication and type(expr.right) is Any:
        tmp = Implication(expr.left, expr.right.val)
        if tmp in expressions:
            if expr.right.var.val not in get_free_variables(expr.left):
                if expr.right.var.val not in free_vars:
                    proved = True
                    cur_type = ("any", tmp)
                else:
                    err = '[Невозможно переделать доказательство. Применение правил с кватором всеобщности, используещее свободную переменную ' \
                          + expr.right.var.__str__() + ' из предположений.]'
            else:
                err = '[Ошибка применения правил вывода с квантором всеобщности. Переменная ' \
                      + expr.right.var.__str__() + ' входит свободно.]'
    return cur_type, err, proved


def check_exists(cur_type, err, expr, expressions, free_vars, proved):
    if type(expr) is Implication and type(expr.left) is Exists:
        tmp = Implication(expr.left.val, expr.right)
        if tmp in expressions:
            if expr.left.var.val not in get_free_variables(expr.right):
                if expr.left.var.val not in free_vars:
                    proved = True
                    cur_type = ("exist", tmp)
                else:
                    err = '[Невозможно переделать доказательство. ' \
                          'Применение правил с кватором существования, используещее свободную переменную ' \
                          + expr.left.var.__str__() + ' из предположений.]'
            else:
                err = '[Ошибка применения правил вывода с квантором существования. Переменная ' \
                      + expr.left.var.__str__() + ' входит свободно.]'
    return cur_type, err, proved


def check_modus_ponens(cur_type, expr, expressions, i, proof, proved):
    for j in range(i - 1, -1, -1):
        mp = Implication(proof[j], expr)
        if parse(str(expr)) == mp:
            print(parse(str(expr)), mp)
        if mp in expressions:
            proved = True
            cur_type = ("modus ponens", proof[j])
            break
    return cur_type, proved


def check_assumptions(assumptions, cur_type, expr, proved):
    if expr in assumptions:
        proved = True
        cur_type = "assumption"
    return cur_type, proved


def check_axioms(cur_type, expr, proved):
    if is_classical_axiom(expr) or is_formal_axiom(expr):
        proved = True
        cur_type = "axiom"
    return cur_type, proved


def main():
    if len(argv) < 2:
        print("expected: python3 hw2.py in.txt (1|0) # 1 -- make deduction proof")
        return
    fin = open(argv[1], "r")
    # fin = open("test.in", "r")
    fout = open("out.txt", "w")
    line, main_expression = fin.readline().rstrip().split("|-")
    assumption, assumptions = get_assumptions(line)
    assumptions.append(assumption)
    free_vars = set()
    if len(assumptions) > 0 and assumptions[0] != '':
        assumptions = [parse(x) for x in assumptions]
        free_vars = get_free_variables(assumptions[-1])
    main_expression = parse(main_expression)
    proof = fin.readlines()
    expressions = set()
    err = '[Недоказаное утверждение]'
    i = 1
    proved = False
    new_proof = []
    for s in proof:
        expr = parse(s)
        proved = False
        cur_type = "unproved"
        cur_type, proved = check_axioms(cur_type, expr, proved)
        if not proved:
            cur_type, proved = check_assumptions(assumptions, cur_type, expr, proved)
        if not proved:
            cur_type, proved = check_modus_ponens(cur_type, expr, expressions, i, proof, proved)
        if not proved:
            cur_type, err, proved = check_exists(cur_type, err, expr, expressions, free_vars, proved)
        if not proved:
            cur_type, err, proved = check_any(cur_type, err, expr, expressions, free_vars, proved)
        if not proved:
            print('Вывод некорректен, начиная с формулы ' + str(i) + ', ' + err + expr.__str__(), file=fout)
            break
        else:
            expressions.add(expr)
            proof[i - 1] = expr
            new_proof.append((expr, cur_type))
            i += 1
    if proved:
        print('Вывод корректен', file=fout)
        if len(assumptions) > 0 and assumptions[0] != '':
            if argv[2] == '1':

                print(
                    ','.join([x.__str__() for x in assumptions[:len(assumptions) - 1]]) + '|-' + Implication(
                        assumptions[-1],
                        main_expression).__str__(),
                    file=fout)
                print('\n'.join([x.__str__() for x in change_proof(new_proof, assumptions[-1])]), file=fout)
    fin.close()
    fout.close()


if __name__ == '__main__':
    main()