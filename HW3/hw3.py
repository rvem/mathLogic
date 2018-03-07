def proof_less(a, b):
    get_evidence("a+0=a", ["a"])
    get_evidence("a+b'=(a+b)'", ["b", "a"])
    get_evidence("a=b->a'=b'", ["b", "a"])
    get_evidence("a'=b'->a=b", ["b", "a"])
    step1 = ["@a@b(a+b'=(a+b)')->@b(_d+b'=(_d+b)')",
             "@b(_d+b'=(_d+b)')",
             "@b(_d+b'=(_d+b)')->(_d+_e'=(_d+_e)')",
             "_d+_e'=(_d+_e)'"]
    mapping = {}
    for i in range(b - a):
        mapping['d'] = '0' + "\'" * a
        mapping['e'] = '0' + "\'" * (b - a - i - 1)
        for s in step1:
            print(fill_vars(s, mapping), file=fout)
    mapping['d'] = '0' + "\'" * a
    print(fill_vars("@a(a+0=a)->(_d+0=_d)", mapping), file=fout)
    print(fill_vars("_d+0=_d", mapping), file=fout)
    step2 = ["@a@b@c(b=a->a=c->b=c)->@b@c(b=_d->_d=c->b=c)",
             "@b@c(b=_d->_d=c->b=c)",
             "@b@c(b=_d->_d=c->b=c)->@c(_e=_d->_d=c->_e=c)",
             "@c(_e=_d->_d=c->_e=c)",
             "@c(_e=_d->_d=c->_e=c)->(_e=_d->_d=_f->_e=_f)",
             "_e=_d->_d=_f->_e=_f",
             "@a@b(a=b->a'=b')->@b(_r=b->_r'=b')",
             "@b(_r=b->_r'=b')",
             "@b(_r=b->_r'=b')->(_r=_k->_r'=_k')",
             "_r=_k->_r'=_k'",
             "_r'=_k'",
             "_d=_f->_e=_f",
             "_e=_f"]
    for i in range(b - a):
        mapping['e'] = '0' + '\'' * a + '+' + '0' + '\'' * (i + 1)
        mapping['d'] = '(' + '0' + '\'' * a + '+' + '0' + '\'' * i + ")\'"
        mapping['f'] = '0' + '\'' * (a + i + 1)
        mapping['k'] = '0' + '\'' * (a + i)
        mapping['r'] = '(' + '0' + '\'' * a + '+' + '0' + '\'' * i + ')'
        for s in step2:
            print(fill_vars(s, mapping), file=fout)
    print('0' + '\'' * a + '+' '0' + '\'' * (b - a) + '='
          + '0' + '\'' * b + "->" + "?p(" + '0' + '\'' * a
          + "+p=" + '0' + '\'' * b + ')', file=fout)
    print("?p(" + '0' + '\'' * a
          + "+p=" + '0' + '\'' * b + ')', file=fout)


def proof_more(a, b):
    get_evidence("!(a'=0)", ["a"])
    print("@a!(a'=0)->!((" + '0' + "\'" * (a - b - 1) + "+p)'=0)", file=fout)
    print("!(" + '0' + "\'" * (a - b - 1) + "+p)'=0", file=fout)
    step1 = ["@e@c(c'+p=e->(c+p)'=e)->@c(c'+p=_t->(c+p)'=_t)",
             "@c(c'+p=_t->(c+p)'=_t)",
             "@c(c'+p=_t->(c+p)'=_t)->(_r'+p=_t->(_r+p)'=_t)",
             "(_r'+p=_t->(_r+p)'=_t)",
             "!(_r+p)'=_t->_r'+p=_t->!(_r+p)'=_t",
             "_r'+p=_t->!(_r+p)'=_t",
             "(_r'+p=_t->(_r+p)'=_t)->(_r'+p=_t->!(_r+p)'=_t)->!_r'+p=_t",
             "(_r'+p=_t->!(_r+p)'=_t)->!_r'+p=_t",
             "!_r'+p=_t"]
    step2 = ["@a@b(!(a=b)->!(a'=b'))->@b(!((_r+p)=b)->!((_r+p)'=b'))",
             "@b(!((_r+p)=b)->!((_r+p)'=b'))",
             "@b(!((_r+p)=b)->!((_r+p)'=b'))->!((_r+p)=_t)->!((_r+p)'=_t')",
             "!((_r+p)=_t)->!((_r+p)'=_t')",
             "!((_r+p)'=_t')"]
    mapping = {}
    for i in range(b + 1):
        mapping['r'] = '0' + "\'" * (a - b + i - 1)
        mapping['t'] = '0' + "\'" * i
        for s in step1:
            print(fill_vars(s, mapping), file=fout)
        if i != b:
            mapping['r'] = '0' + "\'" * (a - b + i)
            for s in step2:
                print(fill_vars(s, mapping), file=fout)
    mapping['b'] = '0' + "\'" * a + "+p=" + '0' + "\'" * b
    mapping['a'] = "(0=0->0=0->0=0)"
    for s in lemma2:
        print(fill_vars(s, mapping), file=fout)
    mapping['b'] = '0' + "\'" * a + "+p=" + '0' + "\'" * b
    mapping['a'] = "!(0=0->0=0->0=0)"
    for s in lemma2:
        print(fill_vars(s, mapping), file=fout)
    s = '!' + '0' + "\'" * a + "+p=" + '0' + "\'" * b
    print(s + "->(0=0->0=0->0=0)->" + s, file=fout)
    print("(0=0->0=0->0=0)->" + s, file=fout)
    print(s + "->!(0=0->0=0->0=0)->" + s, file=fout)
    print("!(0=0->0=0->0=0)->" + s, file=fout)
    s = '0' + "\'" * a + "+p=" + '0' + "\'" * b
    print(s + "->!(0=0->0=0->0=0)", file=fout)
    print(s + "->!!(0=0->0=0->0=0)", file=fout)
    s1 = "?p(" + s + ")->!(0=0->0=0->0=0)"
    s2 = "?p(" + s + ")->!!(0=0->0=0->0=0)"
    print(s1, file=fout)
    print(s2, file=fout)
    print("(" + s1 + ")->(" + s2 + ")->!?p(" + s + ")", file=fout)
    print("(" + s2 + ")->!?p(" + s + ")", file=fout)
    print("!?p(" + s + ")", file=fout)


def get_evidence(s, vars):
    print(s, file=fout)
    print("0=0->0=0->0=0", file=fout)
    print("(" + s + ")->(0=0->0=0->0=0)->(" + s + ")", file=fout)
    print("(0=0->0=0->0=0)->(" + s + ")", file=fout)
    s1 = "(" + s + ")"
    for var in vars:
        print("(0=0->0=0->0=0)->" + s1, file=fout)
        s1 = "@" + var + s1
        print("(0=0->0=0->0=0)->" + s1, file=fout)
    print(s1, file=fout)


def fill_vars(s, mapping):
    res = ''
    underline = False
    for i in range(len(s)):
        if underline:
            underline = False
            continue
        if s[i] == '_':
            res += mapping.get(s[i + 1])
            underline = True
        else:
            res += s[i]
    return res


fin = open("test.in", "r")
fout = open("test.out", "w")
lemma1 = [x.strip() for x in open("lemma1", "r").readlines()]
lemma2 = [x.strip() for x in open("lemma2", "r").readlines()]

a, b = [int(x) for x in fin.readline().split()]
if a <= b:
    print("|-?p(0" + '\'' * a + "+p=0" + '\'' * b + ")", file=fout)
else:
    print("|-!?p(0" + '\'' * a + "+p=0" + '\'' * b + ")", file=fout)

for s in lemma1:
    print(s, file=fout)
if a <= b:
    proof_less(a, b)
else:
    proof_more(a, b)
# print(fill_vars("@c(c'+p=_t->(c+p)'=_t)", {"t": "x"}))
