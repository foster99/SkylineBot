import copy

import matplotlib.pyplot as plt


class Skyline:
    """
    Attributes
    ----------
    buildings : [Buildings]
        List of buildings which conform the skyline.
    """

    def __init__(self):
        self.buildings = []
        self.min = 0
        self.max = 0
        self.width = 0
        self.height = 0

    def clone(self):
        return copy.deepcopy(self)

    def insert_building(self, xmin, h, xmax):

        # if not (xmin < xmax & h > 0):
        #     # raise error en la entrada
        #     return
        if len(self.buildings) == 0:
            self.min = xmin
            self.max = xmax
            self.height = h
            self.width = self.max - self.min
        else:
            # Check boundaries
            if h > self.height:
                self.height = h
            if xmin < self.min | xmax > self.max:
                if xmin < self.min:
                    self.min = xmin
                if xmax > self.max:
                    self.max = xmax
                self.width = self.max - self.min

        self.buildings += [self.Building(xmin, h, xmax)]

    def union(self, s):
        if s.height > self.height:
            self.height = s.height
        if s.min < self.min | s.max > self.max:
            if s.min < self.min:
                self.min = s.min
            if s.max > self.max:
                self.max = s.max
            self.width = self.max - self.min

        self.buildings = self.buildings + s.buildings

    # TODO: def intersection(self):

    def invert(self):
        for b in self.buildings:
            b.invert(self.width, self.min)

    def translate(self, offset):
        self.min += offset
        self.max += offset
        for b in self.buildings:
            b.translate(offset)

    def replicate(self, n):
        if n < 2:
            if n == 0:
                self.buildings = []
            return

        total = self.width
        print(total)

        for i in range(n):
            aux = self.clone()
            aux.translate(i * total)
            self.union(aux)

    def plot(self):
        plt.figure()
        for b in self.buildings:
            b.plot()
        plt.savefig("tmp.png")

    class Building:
        """
        A class used to represent a building.

        Attributes
        ----------
        xmin : int
            Building's start x-coord.
        xmax : int
            Building's end x-coord.
        w : int
            Building's width.
        h : int
            Building's heigth.

        Methods
        ----------
        """

        def __init__(self, xmin, h, xmax):
            """
            Parameters
            ----------
            xmin : int
                Building's start x-coord.
            xmax : int
                Building's end x-coord.
            h : int
                Building's height.
            """
            self.xmin = xmin
            self.xmax = xmax
            self.w = xmax - xmin
            self.h = h

        def invert(self, W, d0):
            """
            Parameters
            ----------
            W : int
                Associated Skyline's total width.
            d0 : int
                Associated Skyline's distance to origin.
            """
            self.xmin = -self.xmin - self.w + W + (2 * d0)
            self.xmax = self.xmin + self.w

        def translate(self, offset):
            self.xmin += offset
            self.xmax += offset

        def plot(self):
            plt.bar(self.xmin + (self.w / 2), self.h, self.w)


x = Skyline()
x.insert_building(1, 5, 2)
x.insert_building(2, 2, 3)
# x.plot()

y = x.clone()
y.insert_building(7, 9, 8)
# y.plot()

# a = Skyline()
# a.insert_building(1,5,2)
# a.insert_building(2,4,3)
# a.insert_building(3,8,5)
# a.translate(4)
# a.insert_building(1,5,2)
# a.invert()
# a.translate(6)
#
# b = Skyline()
# b.insert_building(9,4,11)
# b.insert_building(2,4,3)
# b.invert()
# a.insert_building(3,8,5)
# c = a.clone()
# c.union(b)

# name_user = "salu2"
#
# xmin1 = 2
# xmax1 = 4
# h1 = 8
# w1 = xmax1 - xmin1
#
# xmin2 = 4
# xmax2 = 5
# h2 = 4
# w2 = xmax2 - xmin2
#
# w = w1 + w2
#
# xmin1 = -xmax1 + 2 * w1
# xmin2 = -xmax2 + 2 * w2
#
# plt.bar(xmin1 + (w1 / 2), h1, w1)
# plt.bar(xmin2 + (w2 / 2), h2, w2)
#
# plt.savefig(name_user + "_tmp.png")  # Guardar en un archivo

# Guardar imagen en un objeto
# import io
# from PIL import Image
# import matplotlib.pyplot as plt
#
# plt.figure()
# plt.plot([1, 2])
# plt.title("test")
# buf = io.BytesIO()
# plt.savefig(buf, format='png')
# buf.seek(0)
# im = Image.open(buf)
# im.show()
# buf.close()
