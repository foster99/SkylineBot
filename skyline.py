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
    min : int
        Skyline's starting x-coord.
    max : int
        Skyline's ending x-coord.
    width : int
        Skyline's width.
    height : int
        Skyline's height.
    area : int
        Skyline's area.
    """

    def __init__(self, *args):

        self.buildings = []
        self.min = 0
        self.max = 0
        self.width = 0
        self.height = 0
        self.area = 0

        args_list = list(args)
        args_num = len(args_list)

        # Empty constructor
        if args_num == 0:
            pass

        elif args_num == 1 and isinstance(args_list[0], Skyline):
            self.buildings = copy.deepcopy(args_list[0].buildings)
            self.min = args_list[0].min
            self.max = args_list[0].max
            self.width = args_list[0].width
            self.height = args_list[0].height
            self.area = args_list[0].area

        # One building constructor
        elif args_num == 3:
            self.insert_building(args_list[0], args_list[1], args_list[2])

        # list of buildings constructor
        elif args_num == 1:
            for xmin, h, xmax in zip(args_list[0::3], args_list[1::3], args_list[2::3]):
                self.insert_building(xmin, h, xmax)

        # Random constructor
        elif args_num == 5:
            n, hmax, wmax, xmin, xmax = args_list[0], args_list[1], args_list[2], args_list[3], args_list[4]

            random_list = [(xmin, h, xmin + w) for (xmin, h, w) in
                           [(r.randrange(xmin, xmax), r.randrange(0, hmax), r.randrange(1, wmax)) for _ in range(n)]]
            random_list.sort()
            self.insert_buildings(random_list)

        # Incorrect arguments
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
        """
        Clones itself.
        :return: Returns a clone of itself (another Skyline).
        """
        return copy.deepcopy(self)

    def insert_building(self, xmin, h, xmax):
        """
        Inserts one new building with the specified parameters in the skyline.
        :param xmin: Building's starting x coord.
        :param h: Building's height.
        :param xmax: Building's ending x coord.
        """
        self.insert_buildings([(xmin, h, xmax)])

    def insert_buildings(self, buildings):
        """
        Inserts a set of buildings.
        :param buildings: List of buildings specified as tuples of their parameters (xmin,h,xmax).
        """
        for (xmin, h, xmax) in buildings:

            if xmin >= xmax | h < 1:
                print("Non-valid entry!!")
                continue

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
        Binary search of the Building of the list located on x's left side. (in terms of xmin).
        :param x: Building which we are searching.
        :return: Returns de index of the Building located on x's left side.
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
        Binary search of the Building of the list located on x's right side. (in terms of xmax).
        :param x: Building which we are searching.
        :return: Returns de index of the Building located on x's right side.
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
        """
        Inserts the Building in a sorted list, and maintains it sorted and without overlapping.
        :param x: Building which we are inserting.
        """
        buildings = self.buildings
        build_r, build_l = 0, 0

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
                    # Save the no-overlapped right part if exists
                    right_part = copy.deepcopy(aux[0])
                    right_part.xmin = x.xmax
                    right_part.update()
                    if right_part.w > 0:
                        aux.insert(1, right_part)

                    # Change the left side
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
            if b.w > 0 and b.h > x.h:
                # As b is taller than x, we must divide X in two parts, and insert b in the middle.
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
        """
        Makes the union between 'self' and s Skylines, and stores the result on 'self'.
        :param s: Skyline with which we are merging the original.
        """
        for b in s.buildings:
            self.insert_building(b.xmin, b.h, b.xmax)

    def intersection(self, s):
        """
        Makes the intersection between 'self' and s Skylines, and stores the result on 'self'.
        :param s: Skyline with which we are intersecting the original.
        """
        l1: List[Skyline.Building]
        l2: List[Skyline.Building]
        l3: List[Skyline.Building]
        l1, l2, l3 = self.buildings, copy.deepcopy(s.buildings), []
        while l1 and l2:
            e1, e2, end = l1[0], l2[0], False
            l1, l2 = l1[1:], l2[1:]

            # Overlapping condition
            # If at some point any of the lists becomes empty, then there is no overlapping, so we must end.
            while not (e1.xmax > e2.xmin):
                if l1:
                    e1 = l1[0]
                    l1 = l1[1:]
                else:
                    end = True
                    break
            if end:
                break

            while not (e2.xmax > e1.xmin):
                if l2:
                    e2 = l2[0]
                    l2 = l2[1:]
                else:
                    end = True
                    break
            if end:
                break

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
        """
        Inverts the skyline over the x axis.
        """
        for b in self.buildings:
            b.invert(self.width, self.min)

        self.buildings.reverse()

    def translate(self, offset):
        """
        Translates the Skyline over de x-axis an specified offset.
        :param offset: Offset (positive or negative) are we displacing the Skyline over the x-axis.
        """
        self.min += offset
        self.max += offset
        for b in self.buildings:
            b.translate(offset)

    def replicate(self, n):
        """
        Replicates the skyline along the x-axis n times.
        :param n: Times we want to replicate the skyline.
        """
        if n < 2:
            if n == 0:
                self.clear()
            return

        total = self.width
        clones = [self.clone() for _ in range(n)]
        for i in range(n):
            clones[i].translate(i * total)

        self.buildings = [building for clone in clones for building in clone.buildings]
        self.update()

    def update(self):
        """
        Update the Skyline values based on the current buildings inside of self.buildings.
        """
        if self.buildings:
            self.min = self.buildings[0].xmin
            self.max = self.buildings[-1].xmax
            self.width = self.max - self.min
            self.area = sum([b.area() for b in self.buildings])
        else:
            self.clear()

    def clear(self):
        """
        Clears the Skyline. After calling it, the Skyline does not have any building inside of it.
        """
        self.min = 0
        self.max = 0
        self.width = 0
        self.area = 0
        self.buildings = []

    def plot(self):
        """
        Generates the associated plot to the Skyline.
        """
        plt.figure()
        for b in self.buildings:
            b.plot()

    def save_plot(self, filename):
        self.plot()
        plt.title("Skyline")
        plt.savefig(filename)

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
            """
            Translates the Building over de x-axis an specified offset.
            :param offset: Offset (positive or negative) are we displacing the Building over the x-axis.
            """
            self.xmin += offset
            self.xmax += offset

        def area(self):
            """
            Computes the Building's area.
            :return: Returns the Building's area.
            """
            return self.h * self.w

        def update(self):
            """
            Recomputes the building's width.
            """
            self.w = self.xmax - self.xmin

        def plot(self):
            """
            Generates the associated bar graphic to the buildings, and adds it to the current plt figure.
            """
            plt.bar(self.xmin + (self.w / 2), self.h, self.w, color=(0, 0, 0, 1))
