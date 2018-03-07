# Generated from /home/roman/PycharmProjects/mathlogic/HW2/antlr/Expression.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from expression import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("\u00b0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5=\n\5\f\5\16\5@\13")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6X\n\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\bm\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\tw\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u0082")
        buf.write("\n\n\f\n\16\n\u0085\13\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\7\13\u0090\n\13\f\13\16\13\u0093\13\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\5\f\u00a6\n\f\3\f\3\f\3\f\7\f\u00ab\n\f")
        buf.write("\f\f\16\f\u00ae\13\f\3\f\2\7\6\b\22\24\26\r\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\2\2\2\u00b5\2\30\3\2\2\2\4#\3\2\2\2")
        buf.write("\6%\3\2\2\2\b\63\3\2\2\2\nW\3\2\2\2\fY\3\2\2\2\16l\3\2")
        buf.write("\2\2\20v\3\2\2\2\22x\3\2\2\2\24\u0086\3\2\2\2\26\u00a5")
        buf.write("\3\2\2\2\30\31\5\4\3\2\31\32\b\2\1\2\32\3\3\2\2\2\33\34")
        buf.write("\5\6\4\2\34\35\b\3\1\2\35$\3\2\2\2\36\37\5\6\4\2\37 \7")
        buf.write("\3\2\2 !\5\4\3\2!\"\b\3\1\2\"$\3\2\2\2#\33\3\2\2\2#\36")
        buf.write("\3\2\2\2$\5\3\2\2\2%&\b\4\1\2&\'\5\b\5\2\'(\b\4\1\2(\60")
        buf.write("\3\2\2\2)*\f\3\2\2*+\7\4\2\2+,\5\b\5\2,-\b\4\1\2-/\3\2")
        buf.write("\2\2.)\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\7\3\2\2\2\62\60\3\2\2\2\63\64\b\5\1\2\64\65\5\n\6\2\65")
        buf.write("\66\b\5\1\2\66>\3\2\2\2\678\f\3\2\289\7\5\2\29:\5\n\6")
        buf.write("\2:;\b\5\1\2;=\3\2\2\2<\67\3\2\2\2=@\3\2\2\2><\3\2\2\2")
        buf.write(">?\3\2\2\2?\t\3\2\2\2@>\3\2\2\2AB\5\16\b\2BC\b\6\1\2C")
        buf.write("X\3\2\2\2DE\7\6\2\2EF\5\n\6\2FG\b\6\1\2GX\3\2\2\2HI\7")
        buf.write("\7\2\2IJ\5\4\3\2JK\7\b\2\2KL\b\6\1\2LX\3\2\2\2MN\7\t\2")
        buf.write("\2NO\5\f\7\2OP\5\n\6\2PQ\b\6\1\2QX\3\2\2\2RS\7\n\2\2S")
        buf.write("T\5\f\7\2TU\5\n\6\2UV\b\6\1\2VX\3\2\2\2WA\3\2\2\2WD\3")
        buf.write("\2\2\2WH\3\2\2\2WM\3\2\2\2WR\3\2\2\2X\13\3\2\2\2YZ\7\21")
        buf.write("\2\2Z[\b\7\1\2[\r\3\2\2\2\\]\5\f\7\2]^\b\b\1\2^m\3\2\2")
        buf.write("\2_`\7\22\2\2`a\7\7\2\2ab\5\20\t\2bc\7\b\2\2cd\b\b\1\2")
        buf.write("dm\3\2\2\2ef\7\22\2\2fm\b\b\1\2gh\5\22\n\2hi\7\13\2\2")
        buf.write("ij\5\22\n\2jk\b\b\1\2km\3\2\2\2l\\\3\2\2\2l_\3\2\2\2l")
        buf.write("e\3\2\2\2lg\3\2\2\2m\17\3\2\2\2no\5\22\n\2op\b\t\1\2p")
        buf.write("w\3\2\2\2qr\5\22\n\2rs\7\f\2\2st\5\20\t\2tu\b\t\1\2uw")
        buf.write("\3\2\2\2vn\3\2\2\2vq\3\2\2\2w\21\3\2\2\2xy\b\n\1\2yz\5")
        buf.write("\24\13\2z{\b\n\1\2{\u0083\3\2\2\2|}\f\3\2\2}~\7\r\2\2")
        buf.write("~\177\5\24\13\2\177\u0080\b\n\1\2\u0080\u0082\3\2\2\2")
        buf.write("\u0081|\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2")
        buf.write("\2\u0083\u0084\3\2\2\2\u0084\23\3\2\2\2\u0085\u0083\3")
        buf.write("\2\2\2\u0086\u0087\b\13\1\2\u0087\u0088\5\26\f\2\u0088")
        buf.write("\u0089\b\13\1\2\u0089\u0091\3\2\2\2\u008a\u008b\f\3\2")
        buf.write("\2\u008b\u008c\7\16\2\2\u008c\u008d\5\26\f\2\u008d\u008e")
        buf.write("\b\13\1\2\u008e\u0090\3\2\2\2\u008f\u008a\3\2\2\2\u0090")
        buf.write("\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\25\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\b\f")
        buf.write("\1\2\u0095\u0096\7\21\2\2\u0096\u0097\7\7\2\2\u0097\u0098")
        buf.write("\5\20\t\2\u0098\u0099\7\b\2\2\u0099\u009a\b\f\1\2\u009a")
        buf.write("\u00a6\3\2\2\2\u009b\u009c\5\f\7\2\u009c\u009d\b\f\1\2")
        buf.write("\u009d\u00a6\3\2\2\2\u009e\u009f\7\7\2\2\u009f\u00a0\5")
        buf.write("\22\n\2\u00a0\u00a1\7\b\2\2\u00a1\u00a2\b\f\1\2\u00a2")
        buf.write("\u00a6\3\2\2\2\u00a3\u00a4\7\17\2\2\u00a4\u00a6\b\f\1")
        buf.write("\2\u00a5\u0094\3\2\2\2\u00a5\u009b\3\2\2\2\u00a5\u009e")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00ac\3\2\2\2\u00a7")
        buf.write("\u00a8\f\3\2\2\u00a8\u00a9\7\20\2\2\u00a9\u00ab\b\f\1")
        buf.write("\2\u00aa\u00a7\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\27\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\f#\60>Wlv\u0083\u0091\u00a5\u00ac")
        return buf.getvalue()


class ExpressionParser ( Parser ):

    grammarFileName = "Expression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "'|'", "'&'", "'!'", "'('", "')'", 
                     "'@'", "'?'", "'='", "','", "'+'", "'*'", "'0'", "'''" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VariableText", 
                      "PredicateText", "WS" ]

    RULE_parse = 0
    RULE_expression = 1
    RULE_disjunction = 2
    RULE_conjunction = 3
    RULE_unary = 4
    RULE_variable = 5
    RULE_predicat = 6
    RULE_termList = 7
    RULE_term = 8
    RULE_summand = 9
    RULE_multiplied = 10

    ruleNames =  [ "parse", "expression", "disjunction", "conjunction", 
                   "unary", "variable", "predicat", "termList", "term", 
                   "summand", "multiplied" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    VariableText=15
    PredicateText=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = ExpressionParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            localctx.exp = self.expression()
            localctx.result = localctx.exp.result
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.exp = None # DisjunctionContext
            self.first = None # DisjunctionContext
            self.second = None # ExpressionContext

        def disjunction(self):
            return self.getTypedRuleContext(ExpressionParser.DisjunctionContext,0)


        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ExpressionParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                localctx.exp = self.disjunction(0)
                localctx.result =  localctx.exp.result
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                localctx.first = self.disjunction(0)
                self.state = 29
                self.match(ExpressionParser.T__0)
                self.state = 30
                localctx.second = self.expression()
                localctx.result = Implication(localctx.first.result, localctx.second.result)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.first = None # DisjunctionContext
            self.exp = None # ConjunctionContext
            self.second = None # ConjunctionContext

        def conjunction(self):
            return self.getTypedRuleContext(ExpressionParser.ConjunctionContext,0)


        def disjunction(self):
            return self.getTypedRuleContext(ExpressionParser.DisjunctionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_disjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)



    def disjunction(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressionParser.DisjunctionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_disjunction, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            localctx.exp = self.conjunction(0)
            localctx.result =  localctx.exp.result
            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExpressionParser.DisjunctionContext(self, _parentctx, _parentState)
                    localctx.first = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_disjunction)
                    self.state = 39
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 40
                    self.match(ExpressionParser.T__1)
                    self.state = 41
                    localctx.second = self.conjunction(0)
                    localctx.result = Disjunction(localctx.first.result, localctx.second.result) 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ConjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.first = None # ConjunctionContext
            self.exp = None # UnaryContext
            self.second = None # UnaryContext

        def unary(self):
            return self.getTypedRuleContext(ExpressionParser.UnaryContext,0)


        def conjunction(self):
            return self.getTypedRuleContext(ExpressionParser.ConjunctionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_conjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)



    def conjunction(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressionParser.ConjunctionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_conjunction, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            localctx.exp = self.unary()
            localctx.result =  localctx.exp.result
            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExpressionParser.ConjunctionContext(self, _parentctx, _parentState)
                    localctx.first = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conjunction)
                    self.state = 53
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 54
                    self.match(ExpressionParser.T__2)
                    self.state = 55
                    localctx.second = self.unary()
                    localctx.result = Conjunction(localctx.first.result, localctx.second.result) 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.pred = None # PredicatContext
            self.un = None # UnaryContext
            self.exp = None # ExpressionContext
            self.var = None # VariableContext

        def predicat(self):
            return self.getTypedRuleContext(ExpressionParser.PredicatContext,0)


        def unary(self):
            return self.getTypedRuleContext(ExpressionParser.UnaryContext,0)


        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def variable(self):
            return self.getTypedRuleContext(ExpressionParser.VariableContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)




    def unary(self):

        localctx = ExpressionParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unary)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                localctx.pred = self.predicat()
                localctx.result = localctx.pred.result
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(ExpressionParser.T__3)
                self.state = 67
                localctx.un = self.unary()
                localctx.result = Not(localctx.un.result)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(ExpressionParser.T__4)
                self.state = 71
                localctx.exp = self.expression()
                self.state = 72
                self.match(ExpressionParser.T__5)
                localctx.result = localctx.exp.result
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(ExpressionParser.T__6)
                self.state = 76
                localctx.var = self.variable()
                self.state = 77
                localctx.un = self.unary()
                localctx.result = Any(localctx.var.result, localctx.un.result)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(ExpressionParser.T__7)
                self.state = 81
                localctx.var = self.variable()
                self.state = 82
                localctx.un = self.unary()
                localctx.result = Exists(localctx.var.result, localctx.un.result)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.var = None # Token

        def VariableText(self):
            return self.getToken(ExpressionParser.VariableText, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = ExpressionParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            localctx.var = self.match(ExpressionParser.VariableText)
            localctx.result = Variable((None if localctx.var is None else localctx.var.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.var = None # VariableContext
            self.predText = None # Token
            self.list = None # TermListContext
            self.t1 = None # TermContext
            self.t2 = None # TermContext

        def variable(self):
            return self.getTypedRuleContext(ExpressionParser.VariableContext,0)


        def PredicateText(self):
            return self.getToken(ExpressionParser.PredicateText, 0)

        def termList(self):
            return self.getTypedRuleContext(ExpressionParser.TermListContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.TermContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.TermContext,i)


        def getRuleIndex(self):
            return ExpressionParser.RULE_predicat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicat" ):
                listener.enterPredicat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicat" ):
                listener.exitPredicat(self)




    def predicat(self):

        localctx = ExpressionParser.PredicatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_predicat)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                localctx.var = self.variable()
                localctx.result =  localctx.var.result
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                localctx.predText = self.match(ExpressionParser.PredicateText)
                self.state = 94
                self.match(ExpressionParser.T__4)
                self.state = 95
                localctx.list = self.termList()
                self.state = 96
                self.match(ExpressionParser.T__5)
                localctx.result = Predicate((None if localctx.predText is None else localctx.predText.text), localctx.list.result)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                localctx.predText = self.match(ExpressionParser.PredicateText)
                localctx.result = Predicate((None if localctx.predText is None else localctx.predText.text))
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                localctx.t1 = self.term(0)
                self.state = 102
                self.match(ExpressionParser.T__8)
                self.state = 103
                localctx.t2 = self.term(0)
                localctx.result = Equals(localctx.t1.result, localctx.t2.result)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.t = None # TermContext
            self.l = None # TermListContext

        def term(self):
            return self.getTypedRuleContext(ExpressionParser.TermContext,0)


        def termList(self):
            return self.getTypedRuleContext(ExpressionParser.TermListContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_termList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermList" ):
                listener.enterTermList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermList" ):
                listener.exitTermList(self)




    def termList(self):

        localctx = ExpressionParser.TermListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_termList)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                localctx.t = self.term(0)
                localctx.result = []
                localctx.result.append(localctx.t.result)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                localctx.t = self.term(0)
                self.state = 112
                self.match(ExpressionParser.T__9)
                self.state = 113
                localctx.l = self.termList()
                localctx.l.result.insert(0, localctx.t.result)
                localctx.result = localctx.l.result
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.t = None # TermContext
            self.sum = None # SummandContext
            self._summand = None # SummandContext

        def summand(self):
            return self.getTypedRuleContext(ExpressionParser.SummandContext,0)


        def term(self):
            return self.getTypedRuleContext(ExpressionParser.TermContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressionParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            localctx.sum = localctx._summand = self.summand(0)
            localctx.result =  localctx.sum.result
            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExpressionParser.TermContext(self, _parentctx, _parentState)
                    localctx.t = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 122
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 123
                    self.match(ExpressionParser.T__10)
                    self.state = 124
                    localctx.sum = localctx._summand = self.summand(0)
                    localctx.result = Sum(localctx.t.result, localctx._summand.result) 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SummandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.sum = None # SummandContext
            self.mul = None # MultipliedContext

        def multiplied(self):
            return self.getTypedRuleContext(ExpressionParser.MultipliedContext,0)


        def summand(self):
            return self.getTypedRuleContext(ExpressionParser.SummandContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_summand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummand" ):
                listener.enterSummand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummand" ):
                listener.exitSummand(self)



    def summand(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressionParser.SummandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_summand, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            localctx.mul = self.multiplied(0)
            localctx.result =  localctx.mul.result
            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExpressionParser.SummandContext(self, _parentctx, _parentState)
                    localctx.sum = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_summand)
                    self.state = 136
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 137
                    self.match(ExpressionParser.T__11)
                    self.state = 138
                    localctx.mul = self.multiplied(0)
                    localctx.result = Mul(localctx.sum.result, localctx.mul.result) 
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MultipliedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.mul = None # MultipliedContext
            self.txt = None # Token
            self.list = None # TermListContext
            self.var = None # VariableContext
            self.t = None # TermContext

        def VariableText(self):
            return self.getToken(ExpressionParser.VariableText, 0)

        def termList(self):
            return self.getTypedRuleContext(ExpressionParser.TermListContext,0)


        def variable(self):
            return self.getTypedRuleContext(ExpressionParser.VariableContext,0)


        def term(self):
            return self.getTypedRuleContext(ExpressionParser.TermContext,0)


        def multiplied(self):
            return self.getTypedRuleContext(ExpressionParser.MultipliedContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_multiplied

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplied" ):
                listener.enterMultiplied(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplied" ):
                listener.exitMultiplied(self)



    def multiplied(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressionParser.MultipliedContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_multiplied, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 147
                localctx.txt = self.match(ExpressionParser.VariableText)
                self.state = 148
                self.match(ExpressionParser.T__4)
                self.state = 149
                localctx.list = self.termList()
                self.state = 150
                self.match(ExpressionParser.T__5)
                localctx.result = Predicate((None if localctx.txt is None else localctx.txt.text), localctx.list.result)
                pass

            elif la_ == 2:
                self.state = 153
                localctx.var = self.variable()
                localctx.result =  localctx.var.result
                pass

            elif la_ == 3:
                self.state = 156
                self.match(ExpressionParser.T__4)
                self.state = 157
                localctx.t = self.term(0)
                self.state = 158
                self.match(ExpressionParser.T__5)
                localctx.result =  localctx.t.result
                pass

            elif la_ == 4:
                self.state = 161
                self.match(ExpressionParser.T__12)
                localctx.result =  Variable('0')
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExpressionParser.MultipliedContext(self, _parentctx, _parentState)
                    localctx.mul = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplied)
                    self.state = 165
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 166
                    self.match(ExpressionParser.T__13)
                    localctx.result = Next(localctx.mul.result) 
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.disjunction_sempred
        self._predicates[3] = self.conjunction_sempred
        self._predicates[8] = self.term_sempred
        self._predicates[9] = self.summand_sempred
        self._predicates[10] = self.multiplied_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def disjunction_sempred(self, localctx:DisjunctionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def conjunction_sempred(self, localctx:ConjunctionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def summand_sempred(self, localctx:SummandContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def multiplied_sempred(self, localctx:MultipliedContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




