import sys
from antlr4 import *
from SkylineLexer import SkylineLexer as Lexer
from SkylineParser import SkylineParser as Parser
from SkylineVisitor import SkylineVisitor as Visitor

input_stream = InputStream(input('? '))

lexer = Lexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Parser(token_stream)
tree = parser.root() 

visitor = Visitor()
visitor.visit(tree)