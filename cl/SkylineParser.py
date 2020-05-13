# Generated from Skyline.g by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("[\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2\21\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write(")\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4>\n\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4O\n\4")
        buf.write("\f\4\16\4R\13\4\3\5\3\5\3\5\3\5\3\5\5\5Y\n\5\3\5\2\3\6")
        buf.write("\6\2\4\6\b\2\2\2c\2\20\3\2\2\2\4(\3\2\2\2\6=\3\2\2\2\b")
        buf.write("X\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2\3\f\21\3\2\2\2\r\16")
        buf.write("\5\6\4\2\16\17\7\2\2\3\17\21\3\2\2\2\20\n\3\2\2\2\20\r")
        buf.write("\3\2\2\2\21\3\3\2\2\2\22\23\7\21\2\2\23\24\7\3\2\2\24")
        buf.write(")\5\6\4\2\25\26\7\21\2\2\26\27\7\3\2\2\27\30\7\4\2\2\30")
        buf.write("\31\5\b\5\2\31\32\7\5\2\2\32)\3\2\2\2\33\34\7\21\2\2\34")
        buf.write("\35\7\6\2\2\35\36\7\7\2\2\36\37\7\17\2\2\37 \7\b\2\2 ")
        buf.write("!\7\17\2\2!\"\7\b\2\2\"#\7\17\2\2#$\7\b\2\2$%\7\17\2\2")
        buf.write("%&\7\b\2\2&\'\7\17\2\2\')\7\t\2\2(\22\3\2\2\2(\25\3\2")
        buf.write("\2\2(\33\3\2\2\2)\5\3\2\2\2*+\b\4\1\2+,\7\n\2\2,-\5\6")
        buf.write("\4\2-.\7\13\2\2.>\3\2\2\2/\60\7\r\2\2\60>\5\6\4\6\61\62")
        buf.write("\7\4\2\2\62\63\5\b\5\2\63\64\7\5\2\2\64>\3\2\2\2\65\66")
        buf.write("\7\n\2\2\66\67\7\17\2\2\678\7\b\2\289\7\17\2\29:\7\b\2")
        buf.write("\2:;\7\17\2\2;>\7\13\2\2<>\7\21\2\2=*\3\2\2\2=/\3\2\2")
        buf.write("\2=\61\3\2\2\2=\65\3\2\2\2=<\3\2\2\2>P\3\2\2\2?@\f\b\2")
        buf.write("\2@A\7\f\2\2AO\5\6\4\tBC\f\7\2\2CD\7\16\2\2DO\5\6\4\b")
        buf.write("EF\f\13\2\2FG\7\f\2\2GO\7\17\2\2HI\f\n\2\2IJ\7\r\2\2J")
        buf.write("O\7\17\2\2KL\f\t\2\2LM\7\16\2\2MO\7\17\2\2N?\3\2\2\2N")
        buf.write("B\3\2\2\2NE\3\2\2\2NH\3\2\2\2NK\3\2\2\2OR\3\2\2\2PN\3")
        buf.write("\2\2\2PQ\3\2\2\2Q\7\3\2\2\2RP\3\2\2\2ST\5\6\4\2TU\7\b")
        buf.write("\2\2UV\5\b\5\2VY\3\2\2\2WY\5\6\4\2XS\3\2\2\2XW\3\2\2\2")
        buf.write("Y\t\3\2\2\2\b\20(=NPX")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'['", "']'", "':-'", "'{'", "','", 
                     "'}'", "'('", "')'", "'+'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "WS", "WORD" ]

    RULE_root = 0
    RULE_asigancion = 1
    RULE_skyline = 2
    RULE_skyline_list = 3

    ruleNames =  [ "root", "asigancion", "skyline", "skyline_list" ]

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
    NUM=13
    WS=14
    WORD=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asigancion(self):
            return self.getTypedRuleContext(SkylineParser.AsigancionContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 14
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.asigancion()
                self.state = 9
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.skyline(0)
                self.state = 12
                self.match(SkylineParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsigancionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(SkylineParser.WORD, 0)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def skyline_list(self):
            return self.getTypedRuleContext(SkylineParser.Skyline_listContext,0)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_asigancion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsigancion" ):
                return visitor.visitAsigancion(self)
            else:
                return visitor.visitChildren(self)




    def asigancion(self):

        localctx = SkylineParser.AsigancionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_asigancion)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(SkylineParser.WORD)
                self.state = 17
                self.match(SkylineParser.T__0)
                self.state = 18
                self.skyline(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(SkylineParser.WORD)
                self.state = 20
                self.match(SkylineParser.T__0)
                self.state = 21
                self.match(SkylineParser.T__1)
                self.state = 22
                self.skyline_list()
                self.state = 23
                self.match(SkylineParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(SkylineParser.WORD)
                self.state = 26
                self.match(SkylineParser.T__3)
                self.state = 27
                self.match(SkylineParser.T__4)
                self.state = 28
                self.match(SkylineParser.NUM)
                self.state = 29
                self.match(SkylineParser.T__5)
                self.state = 30
                self.match(SkylineParser.NUM)
                self.state = 31
                self.match(SkylineParser.T__5)
                self.state = 32
                self.match(SkylineParser.NUM)
                self.state = 33
                self.match(SkylineParser.T__5)
                self.state = 34
                self.match(SkylineParser.NUM)
                self.state = 35
                self.match(SkylineParser.T__5)
                self.state = 36
                self.match(SkylineParser.NUM)
                self.state = 37
                self.match(SkylineParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)


        def skyline_list(self):
            return self.getTypedRuleContext(SkylineParser.Skyline_listContext,0)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def WORD(self):
            return self.getToken(SkylineParser.WORD, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_skyline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline" ):
                return visitor.visitSkyline(self)
            else:
                return visitor.visitChildren(self)



    def skyline(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.SkylineContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_skyline, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 41
                self.match(SkylineParser.T__7)
                self.state = 42
                self.skyline(0)
                self.state = 43
                self.match(SkylineParser.T__8)
                pass

            elif la_ == 2:
                self.state = 45
                self.match(SkylineParser.T__10)
                self.state = 46
                self.skyline(4)
                pass

            elif la_ == 3:
                self.state = 47
                self.match(SkylineParser.T__1)
                self.state = 48
                self.skyline_list()
                self.state = 49
                self.match(SkylineParser.T__2)
                pass

            elif la_ == 4:
                self.state = 51
                self.match(SkylineParser.T__7)
                self.state = 52
                self.match(SkylineParser.NUM)
                self.state = 53
                self.match(SkylineParser.T__5)
                self.state = 54
                self.match(SkylineParser.NUM)
                self.state = 55
                self.match(SkylineParser.T__5)
                self.state = 56
                self.match(SkylineParser.NUM)
                self.state = 57
                self.match(SkylineParser.T__8)
                pass

            elif la_ == 5:
                self.state = 58
                self.match(SkylineParser.WORD)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 61
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 62
                        self.match(SkylineParser.T__9)
                        self.state = 63
                        self.skyline(7)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 64
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 65
                        self.match(SkylineParser.T__11)
                        self.state = 66
                        self.skyline(6)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 67
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 68
                        self.match(SkylineParser.T__9)
                        self.state = 69
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 70
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 71
                        self.match(SkylineParser.T__10)
                        self.state = 72
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 73
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 74
                        self.match(SkylineParser.T__11)
                        self.state = 75
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Skyline_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def skyline_list(self):
            return self.getTypedRuleContext(SkylineParser.Skyline_listContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_skyline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline_list" ):
                return visitor.visitSkyline_list(self)
            else:
                return visitor.visitChildren(self)




    def skyline_list(self):

        localctx = SkylineParser.Skyline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_skyline_list)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.skyline(0)
                self.state = 82
                self.match(SkylineParser.T__5)
                self.state = 83
                self.skyline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.skyline(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.skyline_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def skyline_sempred(self, localctx:SkylineContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         




