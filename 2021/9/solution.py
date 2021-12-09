from aoc_utils import aoc_utils
from tests import cases


class HeightMap():
    def __init__(self, hmap):
        self.hmap = hmap
        self.height = len(hmap) - 1
        self.width = len(hmap[0]) - 1
        self.current_pos = [0, 0]
        self.total_risk_level = 0

    def scan(self):
        for y in range(self.height):
            for x in range(self.width):
                current_risk = self.hmap[y][x]
                if current_risk < min(self.check_surrounding(y, x)):
                    print(current_risk)
                    self.total_risk_level += (current_risk + 1)

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

    def check_surrounding(self, y, x):
        surrounding = []
        for f in [self.up, self.down, self.left, self.right]:
            risk = f(y, x)
            if risk: surrounding.append(risk)
       
        return surrounding

def answer(problem_input, level, test=False):
    height_map = HeightMap([[int(i) for i in list(line)] for line in problem_input.splitlines()])
    height_map.scan()
    return height_map.total_risk_level


aoc_utils.run(answer, cases)
