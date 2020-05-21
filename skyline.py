import copy
import random as r
from typing import List

import matplotlib.pyplot as plt


class Skyline:
    """
    Attributes
    ----------
    buildings : [Buildings]
        List of buildings which conform the skyline.
    """

    def __init__(self, *args):
        args_list = list(args)
        args_num = len(args_list)

        self.buildings = []
        self.min = 0
        self.max = 0
        self.width = 0
        self.height = 0
        self.area = 0

        if args_num == 0:
            pass
        elif args_num == 3:  # one building constructor
            self.insert_building(args_list[0], args_list[1], args_list[2])
        elif args_num == 1:  # list of buildings constructor
            for xmin, h, xmax in zip(args_list[0::3], args_list[1::3], args_list[2::3]):
                self.insert_building(xmin, h, xmax)
        elif args_num == 5:  # random constructor
            n, hmax, wmax, xmin, xmax = args_list[0], args_list[1], args_list[2], args_list[3], args_list[4]

            random_list = [(xmin, h, xmin + w) for (xmin, h, w) in
                           [(r.randrange(xmin, xmax), r.randrange(1, hmax), r.randrange(1, wmax)) for _ in range(n)]]
            random_list.sort()
            self.insert_buildings(random_list)
        else:
            print("Wrong Skyline constructor arguments!")
            # error = True

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
        self.insert_buildings([(xmin, h, xmax)])

    def insert_buildings(self, buildings):
        for (xmin, h, xmax) in buildings:

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

    def bisect_xmin(self, x):
        """
        WOW
        """
        lo, hi = 0, len(self.buildings)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.buildings[mid].xmin <= x.xmin:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1

    def bisect_xmax(self, x):
        """
        WOW
        """
        lo, hi = 0, len(self.buildings)
        while lo < hi:
            mid = (lo + hi) // 2
            if x.xmax > self.buildings[mid].xmax:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def sorted_insert(self, x):
        buildings = self.buildings

        # Look for the building located in its left side
        no_left_side = x.xmin < buildings[0].xmin
        if no_left_side:  # there is no one on the left side
            new_list_l = []
        else:
            build_l = self.bisect_xmin(x)
            new_list_l = buildings[:build_l]

        # Look for the building located in its right side
        no_right_side = buildings[-1].xmax < x.xmax
        if no_right_side:  # there is no one on the right side
            new_list_r = []
        else:
            build_r = self.bisect_xmax(x)
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
                new_list_r.insert(0, aux[-1])
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
                    new_list_mid.append(cpy)
                new_list_mid.append(b)
                # Modify X: from b.xmax to x.max
                x.xmin = b.xmax
                x.update()

        self.buildings = new_list_l + new_list_mid + [x] + new_list_r

    def union(self, s):
        for b in s.buildings:
            self.insert_building(b.xmin, b.h, b.xmax)

    def intersection(self, s):
        l1: List[Skyline.Building]
        l2: List[Skyline.Building]
        l3: List[Skyline.Building]
        l1, l2, l3 = self.buildings, copy.deepcopy(s.buildings), []
        while l1 and l2:
            e1, e2, end = l1[0], l2[0], False
            l1 , l2 = l1[1:], l2[1:]

            # Overlapping condition
            # If at some point any of the lists becomes empty, then there is no overlapping, so we must end.
            while not (e1.xmax > e2.xmin):
                if l1:
                    e1 = l1[0]
                    l1 = l1[1:]
                else:
                    end = True
                    break
            if end: break

            while not (e2.xmax > e1.xmin):
                if l2:
                    e2 = l2[0]
                    l2 = l2[1:]
                else:
                    end = True
                    break
            if end: break

            # Compute overlapped building
            xmin = max(e1.xmin, e2.xmin)
            xmax = min(e1.xmax, e2.xmax)
            h = min(e1.h, e2.h)

            # Save overlapped building
            e3 = Skyline.Building(xmin, h, xmax)
            l3.append(e3)

            # We must push into de lists the remaining part of the intersected buildings (just the right one).
            if e1.xmax < e2.xmax:
                e2.xmin = e3.xmax
                e2.update()
                l2.insert(0, e2)
            elif e1.xmax > e2.xmax:
                e1.xmin = e3.xmax
                e1.update()
                l1.insert(0, e1)

        self.buildings = l3
        self.update()

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
        if self.buildings:
            self.min = self.buildings[0].xmin
            self.max = self.buildings[-1].xmax
            self.width = self.max - self.min
            self.area = sum([b.area() for b in self.buildings])
        else:
            self.min = 0
            self.max = 0
            self.width = 0
            self.area = 0

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
            Building's height.

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
            return self.xmin, self.max, self.h

        def plot(self):
            plt.bar(self.xmin + (self.w / 2), self.h, self.w, color=(0, 0, 0, 1))


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
