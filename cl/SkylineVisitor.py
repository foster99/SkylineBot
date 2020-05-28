# Generated from Skyline.g by ANTLR 4.8
import copy

from antlr4 import *

from skyline import Skyline

if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser


# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):
    def __init__(self, user_skylines):
        self.user_skylines = user_skylines

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx: SkylineParser.RootContext):
        nodes = [w for w in ctx.children]
        return self.visit(nodes[0])

    # Visit a parse tree produced by SkylineParser#assignment.
    def visitAssignment(self, ctx: SkylineParser.AssignmentContext):
        nodes = [w for w in ctx.children]
        name: str = nodes[0].getText()
        new_skyline = Skyline(self.visit(nodes[2]))
        print(name, self.user_skylines)
        self.user_skylines[name] = new_skyline
        print(name, self.user_skylines)
        return new_skyline

    # Visit a parse tree produced by SkylineParser#temp_skyline.
    def visitTemp_skyline(self, ctx: SkylineParser.Temp_skylineContext):
        nodes = [w for w in ctx.children]
        new_skyline = Skyline(self.visit(nodes[0]))
        return new_skyline

    # Visit a parse tree produced by SkylineParser#skyline.
    def visitSkyline(self, ctx: SkylineParser.SkylineContext) -> Skyline:
        nodes = [w for w in ctx.children]
        if ctx.mirror():
            skln = Skyline(self.visit(nodes[1]))
            skln.invert()
            return skln
        if ctx.translate_r():
            skln = Skyline(self.visit(nodes[0]))
            offset = int(nodes[2].getText())
            skln.translate(offset)
            return skln
        if ctx.translate_l():
            skln = Skyline(self.visit(nodes[0]))
            offset = - int(nodes[2].getText())
            skln.translate(offset)
            return skln
        if ctx.replicate():
            skln = Skyline(self.visit(nodes[0]))
            n = int(nodes[2].getText())
            skln.replicate(n)
            return skln
        if ctx.union():
            skln1: Skyline = self.visit(nodes[0])
            skln2: Skyline = self.visit(nodes[2])
            skln = skln1.clone()
            skln.union(skln2)
            return skln
        if ctx.intersection():
            skln1: Skyline = self.visit(nodes[0])
            skln2: Skyline = self.visit(nodes[2])
            skln = skln1.clone()
            skln.intersection(skln2)
            return skln
        if ctx.existing_skyline():
            name: str = nodes[0].getText()
            skln = self.user_skylines[name]
            if skln is None:
                print("Skyline inexistente!!")
            return skln
        if ctx.random_skyline():
            return self.visit(nodes[1])
        if ctx.building_list():
            skln: Skyline = Skyline()
            buildings = self.visit(nodes[1])
            skln.insert_buildings(buildings)
            return skln
        if ctx.building():
            (xmin, h, xmax) = self.visit(nodes[1])
            if xmax <= xmin:
                print("Invalid x-coord range!!")
                return Skyline()
            if h < 1:
                print("Invalid height!!")
                return Skyline()
            return Skyline(xmin, h, xmax)

        # Between brackets skyline
        return self.visit(nodes[1])

    # Visit a parse tree produced by SkylineParser#random_skyline.
    def visitRandom_skyline(self, ctx: SkylineParser.Random_skylineContext):
        nodes = [w for w in ctx.children]

        n = int(nodes[0].getText())
        if n < 1:
            print("Invalid N!!")
            return Skyline()

        hmax = int(nodes[2].getText())
        if hmax < 1:
            print("Invalid height!!")
            return Skyline()

        wmax = int(nodes[4].getText())
        if wmax < 1:
            print("Invalid width!!")
            return Skyline()

        xmin = int(nodes[6].getText())
        xmax = int(nodes[8].getText())
        if xmax <= xmin:
            print("Invalid x-coord range!!")
            return Skyline()

        return Skyline(n, hmax, wmax, xmin, xmax)

    # Visit a parse tree produced by SkylineParser#building.
    def visitBuilding(self, ctx: SkylineParser.BuildingContext):
        nodes = [w for w in ctx.children]
        xmin = int(nodes[0].getText())
        h = int(nodes[2].getText())
        xmax = int(nodes[4].getText())
        return xmin, h, xmax

    # Visit a parse tree produced by SkylineParser#building_list.
    def visitBuilding_list(self, ctx: SkylineParser.Building_listContext):
        nodes = [w for w in ctx.children]
        return [self.visit(nodes[1])] + [self.visit(building) for building in nodes[5::4]]  # Take the numbers

    # Visit a parse tree produced by SkylineParser#mirror.
    def visitMirror(self, ctx: SkylineParser.MirrorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#intersection.
    def visitIntersection(self, ctx: SkylineParser.IntersectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#union.
    def visitUnion(self, ctx: SkylineParser.UnionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#translate_r.
    def visitTranslate_r(self, ctx: SkylineParser.Translate_rContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#translate_l.
    def visitTranslate_l(self, ctx: SkylineParser.Translate_lContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#replicate.
    def visitReplicate(self, ctx: SkylineParser.ReplicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#existing_skyline.
    def visitExisting_skyline(self, ctx: SkylineParser.Existing_skylineContext):
        return self.visitChildren(ctx)

del SkylineParser
