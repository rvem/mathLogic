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
        self.__rehash()

    def __str__(self):
        return "(" + self.left.__str__() + self.name + self.right.__str__() + ")"

    def __rehash(self):
        self.hash = (5 * self.name.__hash__() + 13 * self.left.__hash__() ** 3 + 31 * self.right.__hash__() ** 7) % MOD


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

    def __rehash(self):
        self.hash = self.val.__hash__()


class Not(Unary):
    name = "!"

    def __init__(self, value):
        super().__init__(value)
        self.__rehash()

    def __rehash(self):
        self.hash = (5 * self.val.__hash__() ** 3 + 11 * self.name.__hash__()) % MOD

    def __str__(self):
        return "(!" + self.val.__str__() + ")"


# formal expressions

class Any(Unary):
    name = '@'

    def __init__(self, var, value):
        super().__init__(value)
        self.var = var
        self.__rehash()

    def __str__(self):
        return "(@" + self.var.__str__() + self.val.__str__() + ")"

    def __rehash(self):
        self.hash = (23 * self.var.__hash__() ** 3 + 7 * self.val.__hash__() ** 5 + 11 * self.name.__hash__()) % MOD


class Exists(Unary):
    name = '?'

    def __init__(self, var, value):
        super().__init__(value)
        self.var = var
        self.__rehash()

    def __str__(self):
        return "(?" + self.var.__str__() + self.val.__str__() + ")"

    def __rehash(self):
        self.hash = (17 * self.var.__hash__() ** 6 + 31 * self.val.__hash__() ** 7 + 11 * self.name.__hash__() ** 2) % MOD


class Predicate(Unary):
    def __init__(self, name, values=[]):
        self.name = name
        super().__init__(values)
        self.__rehash()

    def __rehash(self):
        self.hash = self.name.__hash__() % MOD
        for values in self.val:
            self.hash *= 41
            self.hash += values.__hash__()

    def __str__(self):
        if len(self.val) == 0:
            return self.name
        result = self.name + "("
        for i in range(len(self.val)):
            if i == len(self.val) - 1:
                result += self.val[i].__str__() + ")"
            else:
                result += self.val[i].__str__() + ","
        return result


class Next(Unary):
    name = "'"

    def __init__(self, value):
        super().__init__(value)
        self.__rehash()

    def __str__(self):
        return self.val.__str__() + self.name

    def __rehash(self):
        self.hash = (19 * self.name.__hash__() ** 3 + 17 * self.val.__hash__()) % MOD


class Sum(Binary):
    name = '+'

    def __init__(self, left, right):
        super().__init__(left, right)


class Mul(Binary):
    name = '*'

    def __init__(self, left, right):
        super().__init__(left, right)


class Equals(Binary):
    name = '='

    def __init__(self, left, right):
        super().__init__(left, right)
