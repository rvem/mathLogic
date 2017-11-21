# Generated from /home/roman/PycharmProjects/mathlogic/HW2/antlr/Expression.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from expression import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\7\20E\n\20\f\20\16\20H\13\20\3\21\3\21")
        buf.write("\7\21L\n\21\f\21\16\21O\13\21\3\22\6\22R\n\22\r\22\16")
        buf.write("\22S\3\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23\3\2")
        buf.write("\3\5\2\13\f\17\17\"\"\2Y\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5(\3\2\2\2\7*\3\2\2\2")
        buf.write("\t,\3\2\2\2\13.\3\2\2\2\r\60\3\2\2\2\17\62\3\2\2\2\21")
        buf.write("\64\3\2\2\2\23\66\3\2\2\2\258\3\2\2\2\27:\3\2\2\2\31<")
        buf.write("\3\2\2\2\33>\3\2\2\2\35@\3\2\2\2\37B\3\2\2\2!I\3\2\2\2")
        buf.write("#Q\3\2\2\2%&\7/\2\2&\'\7@\2\2\'\4\3\2\2\2()\7~\2\2)\6")
        buf.write("\3\2\2\2*+\7(\2\2+\b\3\2\2\2,-\7#\2\2-\n\3\2\2\2./\7*")
        buf.write("\2\2/\f\3\2\2\2\60\61\7+\2\2\61\16\3\2\2\2\62\63\7B\2")
        buf.write("\2\63\20\3\2\2\2\64\65\7A\2\2\65\22\3\2\2\2\66\67\7?\2")
        buf.write("\2\67\24\3\2\2\289\7.\2\29\26\3\2\2\2:;\7-\2\2;\30\3\2")
        buf.write("\2\2<=\7,\2\2=\32\3\2\2\2>?\7\62\2\2?\34\3\2\2\2@A\7)")
        buf.write("\2\2A\36\3\2\2\2BF\4c|\2CE\4\62;\2DC\3\2\2\2EH\3\2\2\2")
        buf.write("FD\3\2\2\2FG\3\2\2\2G \3\2\2\2HF\3\2\2\2IM\4C\\\2JL\4")
        buf.write("\62;\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\"\3\2")
        buf.write("\2\2OM\3\2\2\2PR\t\2\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2")
        buf.write("ST\3\2\2\2TU\3\2\2\2UV\b\22\2\2V$\3\2\2\2\6\2FMS\3\2\3")
        buf.write("\2")
        return buf.getvalue()


class ExpressionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    VariableText = 15
    PredicateText = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'->'", "'|'", "'&'", "'!'", "'('", "')'", "'@'", "'?'", "'='", 
            "','", "'+'", "'*'", "'0'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "VariableText", "PredicateText", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "VariableText", "PredicateText", "WS" ]

    grammarFileName = "Expression.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


