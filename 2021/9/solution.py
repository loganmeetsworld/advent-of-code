from aoc_utils import aoc_utils
from tests import cases


class HeightMap():
    def __init__(self, hmap):
        self.hmap = hmap
        self.height = len(hmap) - 1
        self.width = len(hmap[0]) - 1
        self.total_risk_level = 0

    def scan(self):
        for ypos, y in enumerate(self.hmap):
            for xpos, x in enumerate(y):
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
            if [ypos, xpos] == [1, 9]:
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
    height_map.scan()
    return height_map.total_risk_level


aoc_utils.run(answer, cases)
