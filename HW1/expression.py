MOD = (10 ** 9) + 9


class Expression(object):
    hash = 0

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class Binary(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.rehash()

    def __str__(self):
        return "(" + self.left.__str__() + self.name + self.right.__str__() + ")"

    def rehash(self):
        self.hash = (5 * self.name.__hash__() + 13 * self.left.__hash__() ** 3 + 31 * self.right.__hash__() ** 4) % MOD


class Implication(Binary):
    name = "->"

    def __init__(self, left, right):
        super().__init__(left, right)


class Conjunction(Binary):
    name = "&"

    def __init__(self, left, right):
        super().__init__(left, right)


class Disjunction(Binary):
    name = "|"

    def __init__(self, left, right):
        super().__init__(left, right)


class Unary(Expression):
    def __init__(self, value):
        self.val = value


class Variable(Unary):
    def __init__(self, value):
        self.hash = value.__hash__() % MOD
        super().__init__(value)

    def __str__(self):
        return self.val

    def rehash(self):
        self.hash = self.val.__hash__()


class Not(Unary):
    name = "!"

    def __init__(self, value):
        super().__init__(value)
        self.rehash()

    def rehash(self):
        self.hash = (5 * self.val.__hash__() ** 3 + 11 * self.name.__hash__()) % MOD

    def __str__(self):
        return "(!" + self.val.__str__() + ")"
