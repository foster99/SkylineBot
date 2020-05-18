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

    def insert_building(self, xmin, h, xmax):
        b = self.Building(xmin, h, xmax)
        self.buildings += [b]

    def invert(self,W,d0):
        for b in self.buildings:
            b.invert(W, d0)

    def translate(self, offset):
        for b in self.buildings:
            b.translate(offset)

    def replicate(self, n):
        if n < 2:
            if n == 0: self.buildings = []
            return

        total = len(self.buildings)
        new_buildings = []
        for i in range(n):
            offset = i * total
            new_buildings += [b.translate(offset) for b in self.buildings]

        self.buildings = new_buildings

    def plot(self):
        self.buildings = [b.plot() for b in self.buildings]
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
                Building's heigth.
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



a = Skyline()
a.insert_building(1,5,2)
a.insert_building(2,4,3)
a.insert_building(3,8,5)
a.invert(4,1)
a.translate(4)
a.insert_building(1,5,2)
# a.invert(4,1)
a.translate(-1)
a.insert_building(2,4,3)
a.insert_building(3,8,5)
a.plot()

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
