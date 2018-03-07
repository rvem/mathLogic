from antlr.ExpressionParser import ExpressionParser
from antlr.ExpressionLexer import ExpressionLexer
import antlr4


def parse(s):
    inp = antlr4.InputStream(s)
    lexer = ExpressionLexer(inp)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ExpressionParser(stream)
    expr = parser.parse().result
    return expr
