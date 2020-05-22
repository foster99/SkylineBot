# Generated from Skyline.g by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#asigancion.
    def visitAsigancion(self, ctx:SkylineParser.AsigancionContext):
        l = [w for w in ctx.children]
        print("--------------------")
        print("ID: ", l[0].getText())
        print("operator: ", l[1].getText())
        print("Skyline: ", l[2].getText())
        print("--------------------")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skyline.
    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skyline_root.
    def visitSkyline_root(self, ctx:SkylineParser.Skyline_rootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skyline_list.
    def visitSkyline_list(self, ctx:SkylineParser.Skyline_listContext):
        return self.visitChildren(ctx)



del SkylineParser