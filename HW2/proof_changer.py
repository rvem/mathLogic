from parser import parse

from expression import *


def change_proof(proof, last_assumption):
    new_proof = []
    for expr, expr_type in proof:
        if type(expr_type) is str:
            if expr_type == "axiom":
                new_proof.append(Implication(expr, Implication(last_assumption, expr)))
                new_proof.append(expr)
                new_proof.append(Implication(last_assumption, expr))
            elif expr_type == "assumption":
                if expr == last_assumption:
                    mp1 = Implication(last_assumption, Implication(last_assumption, last_assumption))
                    mp2 = Implication(last_assumption,
                                      Implication(Implication(last_assumption, last_assumption), last_assumption))
                    mp3 = Implication(last_assumption, last_assumption)
                    new_proof.append(mp1)
                    new_proof.append(Implication(mp1, Implication(mp2, mp3)))
                    new_proof.append(Implication(mp2, mp3))
                    new_proof.append(mp2)
                    new_proof.append(mp3)
                else:
                    mp = Implication(last_assumption, expr)
                    new_proof.append(Implication(expr, mp))
                    new_proof.append(expr)
                    new_proof.append(mp)
        else:
            if expr_type[0] == "modus ponens":
                mp1 = Implication(last_assumption, Implication(expr_type[1], expr))
                mp2 = Implication(last_assumption, expr_type[1])
                mp3 = Implication(last_assumption, expr)
                new_proof.append(Implication(mp2, Implication(mp1, mp3)))
                new_proof.append(Implication(mp1, mp3))
                new_proof.append(mp3)
            elif expr_type[0] == "exist":
                for s in exist_rule:
                    tmp = s.replace("$", str(last_assumption)).replace("#", str(expr.left.val))\
                        .replace(":", str(expr.right)).replace(";", str(expr.left.var))
                    new_proof.append(parse(tmp))
            elif expr_type[0] == "any":
                for s in any_rule:
                    tmp = s.replace("$", str(last_assumption)).replace("#", str(expr.left)) \
                        .replace(":", str(expr.right.val)).replace(";", str(expr.right.var))
                    new_proof.append(parse(tmp))
    return new_proof

exist_rule = """#->$->#
$->#->:
($->#->:)->#->$->#->:
#->$->#->:
($->#)->($->#->:)->$->:
(($->#)->($->#->:)->$->:)->#->($->#)->($->#->:)->$->:
#->($->#)->($->#->:)->$->:
(#->$->#)->(#->($->#)->($->#->:)->$->:)->#->($->#->:)->$->:
(#->($->#)->($->#->:)->$->:)->#->($->#->:)->$->:
#->($->#->:)->$->:
(#->$->#->:)->(#->($->#->:)->$->:)->#->$->:
(#->($->#->:)->$->:)->#->$->:
#->$->:
?;#->$->:
$->?;#->$
?;#->$->:
(?;#->$->:)->$->?;#->$->:
$->?;#->$->:
(?;#->$)->(?;#->$->:)->?;#->:
((?;#->$)->(?;#->$->:)->?;#->:)->$->(?;#->$)->(?;#->$->:)->?;#->:
$->(?;#->$)->(?;#->$->:)->?;#->:
($->?;#->$)->($->(?;#->$)->(?;#->$->:)->?;#->:)->$->(?;#->$->:)->?;#->:
($->(?;#->$)->(?;#->$->:)->?;#->:)->$->(?;#->$->:)->?;#->:
$->(?;#->$->:)->?;#->:
($->?;#->$->:)->($->(?;#->$->:)->?;#->:)->$->?;#->:
($->(?;#->$->:)->?;#->:)->$->?;#->:
$->?;#->:""".split('\n')

any_rule = """$->#->:
$&#->$
$&#->#
$->#->:
($->#->:)->$&#->$->#->:
$&#->$->#->:
($&#->$)->($&#->$->#->:)->$&#->#->:
($&#->$->#->:)->$&#->#->:
$&#->#->:
($&#->#)->($&#->#->:)->($&#->:)
($&#->#->:)->($&#->:)
$&#->:
$&#->@;:
$->#->$&#
$&#->@;:
($&#->@;:)->$->$&#->@;:
$->$&#->@;:
($&#->@;:)->#->$&#->@;:
(($&#->@;:)->#->$&#->@;:)->$->($&#->@;:)->#->$&#->@;:
$->($&#->@;:)->#->$&#->@;:
($->$&#->@;:)->($->(($&#->@;:)->#->$&#->@;:))->$->#->$&#->@;:
($->(($&#->@;:)->#->$&#->@;:))->$->#->$&#->@;:
$->#->$&#->@;:
(#->$&#)->(#->$&#->@;:)->#->@;:
((#->$&#)->(#->$&#->@;:)->#->@;:)->$->(#->$&#)->(#->$&#->@;:)->#->@;:
$->(#->$&#)->(#->$&#->@;:)->#->@;:
($->#->$&#)->($->(#->$&#)->(#->$&#->@;:)->#->@;:)->$->(#->$&#->@;:)->#->@;:
($->(#->$&#)->(#->$&#->@;:)->#->@;:)->$->(#->$&#->@;:)->#->@;:
$->(#->$&#->@;:)->#->@;:
($->#->$&#->@;:)->($->(#->$&#->@;:)->#->@;:)->$->#->@;:
($->(#->$&#->@;:)->#->@;:)->$->#->@;:
$->#->@;:""".split('\n')
