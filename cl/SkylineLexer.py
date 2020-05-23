# Generated from Skyline.g by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("N\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\r\3\16\6\16=\n\16\r\16\16\16>")
        buf.write("\3\17\6\17B\n\17\r\17\16\17C\3\17\3\17\3\20\3\20\7\20")
        buf.write("J\n\20\f\20\16\20M\13\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3")
        buf.write("\2\6\3\2\62;\4\2\f\f\"\"\4\2C\\c|\5\2\62;C\\c|\2P\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5$\3\2\2\2\7&\3")
        buf.write("\2\2\2\t(\3\2\2\2\13*\3\2\2\2\r,\3\2\2\2\17.\3\2\2\2\21")
        buf.write("\60\3\2\2\2\23\62\3\2\2\2\25\64\3\2\2\2\27\66\3\2\2\2")
        buf.write("\318\3\2\2\2\33<\3\2\2\2\35A\3\2\2\2\37G\3\2\2\2!\"\7")
        buf.write("<\2\2\"#\7?\2\2#\4\3\2\2\2$%\7*\2\2%\6\3\2\2\2&\'\7+\2")
        buf.write("\2\'\b\3\2\2\2()\7}\2\2)\n\3\2\2\2*+\7\177\2\2+\f\3\2")
        buf.write("\2\2,-\7]\2\2-\16\3\2\2\2./\7_\2\2/\20\3\2\2\2\60\61\7")
        buf.write("/\2\2\61\22\3\2\2\2\62\63\7,\2\2\63\24\3\2\2\2\64\65\7")
        buf.write("-\2\2\65\26\3\2\2\2\66\67\7.\2\2\67\30\3\2\2\289\7.\2")
        buf.write("\29:\7*\2\2:\32\3\2\2\2;=\t\2\2\2<;\3\2\2\2=>\3\2\2\2")
        buf.write("><\3\2\2\2>?\3\2\2\2?\34\3\2\2\2@B\t\3\2\2A@\3\2\2\2B")
        buf.write("C\3\2\2\2CA\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\b\17\2\2F\36")
        buf.write("\3\2\2\2GK\t\4\2\2HJ\t\5\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2")
        buf.write("\2\2KL\3\2\2\2L \3\2\2\2MK\3\2\2\2\6\2>CK\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

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
    NUM = 13
    WS = 14
    WORD = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'('", "')'", "'{'", "'}'", "'['", "']'", "'-'", "'*'", 
            "'+'", "','", "',('" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "WS", "WORD" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "NUM", "WS", 
                  "WORD" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


