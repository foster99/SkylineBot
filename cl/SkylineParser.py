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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\5\2")
        buf.write("\17\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write(")\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\67\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4?\n\4\f\4\16\4")
        buf.write("B\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5L\n\5\3\6\3")
        buf.write("\6\3\6\7\6Q\n\6\f\6\16\6T\13\6\3\6\2\3\6\7\2\4\6\b\n\2")
        buf.write("\4\3\2\f\r\3\2\13\r\2Z\2\16\3\2\2\2\4(\3\2\2\2\6\66\3")
        buf.write("\2\2\2\bK\3\2\2\2\nM\3\2\2\2\f\17\5\4\3\2\r\17\5\6\4\2")
        buf.write("\16\f\3\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20\21\7\2\2\3")
        buf.write("\21\3\3\2\2\2\22\23\7\20\2\2\23\24\7\3\2\2\24)\5\6\4\2")
        buf.write("\25\26\7\20\2\2\26\27\7\3\2\2\27\30\7\4\2\2\30\31\5\n")
        buf.write("\6\2\31\32\7\5\2\2\32)\3\2\2\2\33\34\7\20\2\2\34\35\7")
        buf.write("\3\2\2\35\36\7\6\2\2\36\37\7\16\2\2\37 \7\7\2\2 !\7\16")
        buf.write("\2\2!\"\7\7\2\2\"#\7\16\2\2#$\7\7\2\2$%\7\16\2\2%&\7\7")
        buf.write("\2\2&\'\7\16\2\2\')\7\b\2\2(\22\3\2\2\2(\25\3\2\2\2(\33")
        buf.write("\3\2\2\2)\5\3\2\2\2*+\b\4\1\2+,\7\t\2\2,-\5\6\4\2-.\7")
        buf.write("\n\2\2.\67\3\2\2\2/\60\7\13\2\2\60\67\5\6\4\7\61\62\7")
        buf.write("\4\2\2\62\63\5\n\6\2\63\64\7\5\2\2\64\67\3\2\2\2\65\67")
        buf.write("\5\b\5\2\66*\3\2\2\2\66/\3\2\2\2\66\61\3\2\2\2\66\65\3")
        buf.write("\2\2\2\67@\3\2\2\289\f\5\2\29:\t\2\2\2:?\5\6\4\6;<\f\6")
        buf.write("\2\2<=\t\3\2\2=?\7\16\2\2>8\3\2\2\2>;\3\2\2\2?B\3\2\2")
        buf.write("\2@>\3\2\2\2@A\3\2\2\2A\7\3\2\2\2B@\3\2\2\2CD\7\t\2\2")
        buf.write("DE\7\16\2\2EF\7\7\2\2FG\7\16\2\2GH\7\7\2\2HI\7\16\2\2")
        buf.write("IL\7\n\2\2JL\7\20\2\2KC\3\2\2\2KJ\3\2\2\2L\t\3\2\2\2M")
        buf.write("R\5\6\4\2NO\7\7\2\2OQ\5\6\4\2PN\3\2\2\2QT\3\2\2\2RP\3")
        buf.write("\2\2\2RS\3\2\2\2S\13\3\2\2\2TR\3\2\2\2\t\16(\66>@KR")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'['", "']'", "'{'", "','", "'}'", 
                     "'('", "')'", "'-'", "'+'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "WS", "WORD" ]

    RULE_root = 0
    RULE_asigancion = 1
    RULE_skyline = 2
    RULE_skyline_root = 3
    RULE_skyline_list = 4

    ruleNames =  [ "root", "asigancion", "skyline", "skyline_root", "skyline_list" ]

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
    NUM=12
    WS=13
    WORD=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def asigancion(self):
            return self.getTypedRuleContext(SkylineParser.AsigancionContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 10
                self.asigancion()
                pass

            elif la_ == 2:
                self.state = 11
                self.skyline(0)
                pass


            self.state = 14
            self.match(SkylineParser.EOF)
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
                self.match(SkylineParser.T__0)
                self.state = 27
                self.match(SkylineParser.T__3)
                self.state = 28
                self.match(SkylineParser.NUM)
                self.state = 29
                self.match(SkylineParser.T__4)
                self.state = 30
                self.match(SkylineParser.NUM)
                self.state = 31
                self.match(SkylineParser.T__4)
                self.state = 32
                self.match(SkylineParser.NUM)
                self.state = 33
                self.match(SkylineParser.T__4)
                self.state = 34
                self.match(SkylineParser.NUM)
                self.state = 35
                self.match(SkylineParser.T__4)
                self.state = 36
                self.match(SkylineParser.NUM)
                self.state = 37
                self.match(SkylineParser.T__5)
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


        def skyline_root(self):
            return self.getTypedRuleContext(SkylineParser.Skyline_rootContext,0)


        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 41
                self.match(SkylineParser.T__6)
                self.state = 42
                self.skyline(0)
                self.state = 43
                self.match(SkylineParser.T__7)
                pass

            elif la_ == 2:
                self.state = 45
                self.match(SkylineParser.T__8)
                self.state = 46
                self.skyline(5)
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
                self.skyline_root()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 60
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 54
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.T__9 or _la==SkylineParser.T__10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.skyline(4)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 57
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SkylineParser.T__8) | (1 << SkylineParser.T__9) | (1 << SkylineParser.T__10))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Skyline_rootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def WORD(self):
            return self.getToken(SkylineParser.WORD, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_skyline_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline_root" ):
                return visitor.visitSkyline_root(self)
            else:
                return visitor.visitChildren(self)




    def skyline_root(self):

        localctx = SkylineParser.Skyline_rootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_skyline_root)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(SkylineParser.T__6)
                self.state = 66
                self.match(SkylineParser.NUM)
                self.state = 67
                self.match(SkylineParser.T__4)
                self.state = 68
                self.match(SkylineParser.NUM)
                self.state = 69
                self.match(SkylineParser.T__4)
                self.state = 70
                self.match(SkylineParser.NUM)
                self.state = 71
                self.match(SkylineParser.T__7)
                pass
            elif token in [SkylineParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(SkylineParser.WORD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Skyline_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_skyline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline_list" ):
                return visitor.visitSkyline_list(self)
            else:
                return visitor.visitChildren(self)




    def skyline_list(self):

        localctx = SkylineParser.Skyline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_skyline_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.skyline(0)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__4:
                self.state = 76
                self.match(SkylineParser.T__4)
                self.state = 77
                self.skyline(0)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




