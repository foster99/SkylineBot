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
        self.area = 0

    def __repr__(self):
        return "min    = %s\n" % self.min + \
               "max    = %s\n" % self.max + \
               "width  = %s\n" % self.width + \
               "height = %s\n" % self.height + \
               "area   = %s\n" % self.area + \
               "Buildings(%s):\n" % len(self.buildings) + \
               str(self.buildings)

    def clone(self):
        return copy.deepcopy(self)

    def insert_building(self, xmin, h, xmax):

        if xmin >= xmax | h < 1:
            print("Non-valid entry!!")
            return

        if len(self.buildings) == 0:
            self.min = xmin
            self.max = xmax
            self.height = h
            self.width = self.max - self.min
            self.buildings = [self.Building(xmin, h, xmax)]
        else:
            # Check boundaries
            self.sorted_insert(self.Building(xmin, h, xmax))

            if h > self.height:
                self.height = h
            if xmin < self.min | xmax > self.max:
                if xmin < self.min:
                    self.min = xmin
                if xmax > self.max:
                    self.max = xmax

        self.update()

    def sorted_insert(self, x):

        buildings = self.buildings
        length = len(buildings)

        # Look for the building located in its left side
        no_left_side = x.xmin < buildings[0].xmin
        if no_left_side:  # there is no one on the left side
            new_list_l = []
        else:
            build_l = 0  # index of the building located in its left side
            while build_l + 1 < length and buildings[build_l + 1].xmin <= x.xmin:
                build_l = build_l + 1
            new_list_l = buildings[:build_l]

        # Look for the building located in its right side
        no_right_side = buildings[-1].xmax < x.xmax
        if no_right_side:  # there is no one on the right side
            new_list_r = []
        else:
            build_r = length - 1  # index of the building located in its right side
            while 0 <= build_r - 1 and x.xmax <= buildings[build_r - 1].xmax:
                build_r = build_r - 1
            new_list_r = buildings[build_r + 1:]

        # Bounds treatment
        if no_left_side and no_right_side:
            aux = buildings[:]
        elif no_left_side:
            aux = buildings[:build_r + 1]
        elif no_right_side:
            aux = buildings[build_l:]
        else:
            aux = buildings[build_l:build_r + 1]

        if len(aux) > 0 and not no_left_side:  # There is left bound
            if not aux[0].xmax <= x.xmin:  # There is overlapping
                if aux[0].h >= x.h:  # The old one is taller
                    x.xmin = aux[0].xmax
                    x.update()
                else:  # The new one is taller
                    aux[0].xmax = x.xmin
                    aux[0].update()

            if aux[0].w > 0:  # if is still valid, save it
                new_list_l.append(aux[0])

            aux = aux[1:]  # pop it from aux

        if len(aux) > 0 and not no_right_side:  # There is right bound
            if not x.xmax <= aux[-1].xmin:  # There is overlapping
                if aux[-1].h >= x.h:  # The old one is taller
                    x.xmax = aux[-1].xmin
                    x.update()
                else:  # The new one is taller
                    aux[-1].xmin = x.xmax
                    aux[-1].update()

            if aux[-1].w > 0:  # if is still valid, save it
                new_list_r.insert(0,aux[-1])
            aux = aux[:-1]

        # At this point, there is NO overlapping on the sides
        # The "aux" content are the buildings that are "inside" the new one, in terms of x.

        new_list_mid = []
        for b in aux:
            if b.w > 0 and b.h > x.h:  # As b is taller than x, we must divide X in two parts, and insert b in the middle.
                # Create a copy of X: from x.xmin to b.xmin
                cpy = copy.deepcopy(x)
                cpy.xmax = b.xmin
                cpy.update()
                # Insert the copy and b
                if cpy.w > 0:
                    new_list_mid = new_list_mid + [cpy, b]
                else:
                    new_list_mid = new_list_mid + [b]
                # Modify X: from b.xmax to x.max
                x.xmin = b.xmax
                x.update()

        self.buildings = new_list_l + new_list_mid + [x] + new_list_r

    def sort_buildings(self):
        self.buildings.sort(key=self.Building.sort_key)

    def union(self, s):
        if s.height > self.height:
            self.height = s.height
        if s.min < self.min or s.max > self.max:
            if s.min < self.min:
                self.min = s.min
            if s.max > self.max:
                self.max = s.max
        self.update()

        for b in s.buildings:
            self.insert_building(b.xmin, b.h, b.xmax)

    def intersection(self, s):
        if s.max <= self.min or s.min >= self.max:
            return

    def invert(self):
        for b in self.buildings:
            b.invert(self.width, self.min)

        self.buildings.reverse()

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
        clones = [self.clone() for _ in range(n)]
        for i in range(n):
            clones[i].translate(i * total)

        self.buildings = [building for clone in clones for building in clone.buildings]
        self.update()


    def update(self):
        self.min = self.buildings[0].xmin
        self.max = self.buildings[-1].xmax
        self.width = self.max - self.min
        self.area = sum([b.area() for b in self.buildings])

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

        def __repr__(self):
            return "(%s,%s,%s)" % (self.xmin, self.h, self.xmax)

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

        def area(self):
            return self.h * self.w

        def update(self):
            self.w = self.xmax - self.xmin

        def sort_key(self):
            return (self.xmin, self.max, self.h)

        def plot(self):
            plt.bar(self.xmin + (self.w / 2), self.h, self.w)  # , color=(0, 0, 0, 1))


x = Skyline()
x.insert_building(1, 5, 2)
x.insert_building(2, 2, 3)
# x.plot()

y = x.clone()
y.insert_building(7, 9, 8)
y.insert_building(3, 5, 12)
y.insert_building(4, 6, 10)
y.insert_building(13,15,15)
y.insert_building(15,2,16)
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
