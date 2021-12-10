from math import prod

from aoc_utils import aoc_utils
from tests import cases


class HeightMap():
    def __init__(self, hmap):
        self.hmap = hmap
        self.height = len(hmap) - 1
        self.width = len(hmap[0]) - 1
        self.total_risk_level = 0
        self.basin_areas = []

    def scan_for_basins(self):
        for ypos, y in enumerate(self.hmap):
            for xpos, x in enumerate(y):
                if x == 9: continue
                adjacent = self.check_surrounding(ypos, xpos)
                if x < min(adjacent):
                    basin = [[ypos,xpos]]
                    for r, c in basin:
                        if r - 1 >= 0 and self.hmap[r - 1][c] != 9 and [r - 1,c] not in basin:
                            basin.append([r - 1,c])
                        if r + 1 < len(self.hmap) and self.hmap[r + 1][c] != 9 and [r + 1,c] not in basin:
                            basin.append([r + 1,c])
                        if c - 1 >= 0 and self.hmap[r][c - 1] != 9 and [r, c - 1] not in basin:
                            basin.append([r, c - 1])
                        if c + 1 < len(self.hmap[0]) and self.hmap[r][c + 1] != 9 and [r, c + 1] not in basin:
                            basin.append([r, c + 1])
            
                    self.basin_areas.append(len(basin))

    def scan_for_lowest_levels(self):
        for ypos, y in enumerate(self.hmap):
            for xpos, x in enumerate(y):
                if x == 9: continue
                adjacent = self.check_surrounding(ypos, xpos)
                if x < min(adjacent):
                    self.total_risk_level += (x + 1)

    def left(self, ypos, xpos):
        if 0 <= ypos <= self.height and 0 <= xpos - 1 <= self.width:
            return self.hmap[ypos][xpos - 1]

    def right(self, ypos, xpos):
        if 0 <= ypos <= self.height and 0 <= xpos + 1 <= self.width:
            return self.hmap[ypos][xpos + 1]

    def up(self, ypos, xpos):
        if 0 <= ypos - 1 <= self.height and 0 <= xpos <= self.width:
            return self.hmap[ypos - 1][xpos]

    def down(self, ypos, xpos):
        if 0 <= ypos + 1 <= self.height and 0 <= xpos <= self.width:
            return self.hmap[ypos + 1][xpos]

    def check_surrounding(self, ypos, xpos):
        surrounding = []
        for f in [self.up, self.down, self.left, self.right]:
            risk = f(ypos, xpos)
            if risk or risk == 0: surrounding.append(risk)
       
        return surrounding

def answer(problem_input, level, test=False):
    height_map = HeightMap([[int(i) for i in list(line)] for line in problem_input.splitlines()])
    if level == 1:
        height_map.scan_for_lowest_levels()
        return height_map.total_risk_level
    if level == 2:
        height_map.scan_for_basins()
        return prod(sorted(height_map.basin_areas)[-3:])

aoc_utils.run(answer, cases)
