# Generated from /home/roman/PycharmProjects/mathlogic/HW2/antlr/Expression.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

from expression import *


# This class defines a complete listener for a parse tree produced by ExpressionParser.
class ExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionParser#parse.
    def enterParse(self, ctx:ExpressionParser.ParseContext):
        pass

    # Exit a parse tree produced by ExpressionParser#parse.
    def exitParse(self, ctx:ExpressionParser.ParseContext):
        pass


    # Enter a parse tree produced by ExpressionParser#expression.
    def enterExpression(self, ctx:ExpressionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#expression.
    def exitExpression(self, ctx:ExpressionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#disjunction.
    def enterDisjunction(self, ctx:ExpressionParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#disjunction.
    def exitDisjunction(self, ctx:ExpressionParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#conjunction.
    def enterConjunction(self, ctx:ExpressionParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#conjunction.
    def exitConjunction(self, ctx:ExpressionParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#unary.
    def enterUnary(self, ctx:ExpressionParser.UnaryContext):
        pass

    # Exit a parse tree produced by ExpressionParser#unary.
    def exitUnary(self, ctx:ExpressionParser.UnaryContext):
        pass


    # Enter a parse tree produced by ExpressionParser#variable.
    def enterVariable(self, ctx:ExpressionParser.VariableContext):
        pass

    # Exit a parse tree produced by ExpressionParser#variable.
    def exitVariable(self, ctx:ExpressionParser.VariableContext):
        pass


    # Enter a parse tree produced by ExpressionParser#predicat.
    def enterPredicat(self, ctx:ExpressionParser.PredicatContext):
        pass

    # Exit a parse tree produced by ExpressionParser#predicat.
    def exitPredicat(self, ctx:ExpressionParser.PredicatContext):
        pass


    # Enter a parse tree produced by ExpressionParser#termList.
    def enterTermList(self, ctx:ExpressionParser.TermListContext):
        pass

    # Exit a parse tree produced by ExpressionParser#termList.
    def exitTermList(self, ctx:ExpressionParser.TermListContext):
        pass


    # Enter a parse tree produced by ExpressionParser#term.
    def enterTerm(self, ctx:ExpressionParser.TermContext):
        pass

    # Exit a parse tree produced by ExpressionParser#term.
    def exitTerm(self, ctx:ExpressionParser.TermContext):
        pass


    # Enter a parse tree produced by ExpressionParser#summand.
    def enterSummand(self, ctx:ExpressionParser.SummandContext):
        pass

    # Exit a parse tree produced by ExpressionParser#summand.
    def exitSummand(self, ctx:ExpressionParser.SummandContext):
        pass


    # Enter a parse tree produced by ExpressionParser#multiplied.
    def enterMultiplied(self, ctx:ExpressionParser.MultipliedContext):
        pass

    # Exit a parse tree produced by ExpressionParser#multiplied.
    def exitMultiplied(self, ctx:ExpressionParser.MultipliedContext):
        pass


