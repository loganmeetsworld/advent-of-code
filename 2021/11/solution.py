from aoc_utils import aoc_utils
from tests import cases
   

class OctoMap():
    def __init__(self, omap):
        self.map = omap
        self.height = len(omap) - 1
        self.width = len(omap[0]) - 1
        self.flashed = []
        self.flashes = 0

    def step(self):
        for ypos, y in enumerate(self.map):
            for xpos, x in enumerate(y):
                self.energy_gain(ypos, xpos)

        self.retire_octos()

    def energy_gain(self, ypos, xpos):
        self.map[ypos][xpos] += 1
        if self.map[ypos][xpos] == 10:
            self.flash(ypos, xpos)

    def flash(self, ypos, xpos):
        self.flashes += 1
        self.flashed.append([ypos, xpos])
        neighbors = []
        for f in [self.up, self.down, self.left, self.right, self.upleft, self.upright, self.downleft, self.downright]:
            neighbor = f(ypos, xpos)
            if neighbor: neighbors.append(f(ypos, xpos))

        [self.energy_gain(n[0], n[1]) for n in neighbors]

    def retire_octos(self):
        for flashed in self.flashed:
            self.map[flashed[0]][flashed[1]] = 0

        self.flashed = []

    def left(self, ypos, xpos):
        if 0 <= ypos <= self.height and 0 <= xpos - 1 <= self.width:
            return [ypos, xpos - 1]

    def right(self, ypos, xpos):
        if 0 <= ypos <= self.height and 0 <= xpos + 1 <= self.width:
            return [ypos, xpos + 1]

    def up(self, ypos, xpos):
        if 0 <= ypos - 1 <= self.height and 0 <= xpos <= self.width:
            return [ypos - 1, xpos]

    def down(self, ypos, xpos):
        if 0 <= ypos + 1 <= self.height and 0 <= xpos <= self.width:
            return [ypos + 1, xpos]

    def upright(self, ypos, xpos):
        if 0 <= ypos - 1 <= self.height and 0 <= xpos + 1 <= self.width:
            return [ypos - 1, xpos + 1]

    def upleft(self, ypos, xpos):
        if 0 <= ypos - 1 <= self.height and 0 <= xpos - 1 <= self.width:
            return [ypos - 1, xpos - 1]

    def downright(self, ypos, xpos):
        if 0 <= ypos + 1 <= self.height and 0 <= xpos + 1 <= self.width:
            return [ypos + 1, xpos + 1]

    def downleft(self, ypos, xpos):
        if 0 <= ypos + 1 <= self.height and 0 <= xpos - 1 <= self.width:
            return [ypos + 1, xpos - 1]

    def print_map(self):
        for line in self.map:
            print("".join(['\033[1m' + str(i) + '\033[0m' if i == 0 else str(i) for i in line]))
        print()
        
    def count_lights(self):
        return sum([l.count(0) for l in self.map])


def answer(problem_input, level, test=False):
    octopuses = OctoMap([[int(i) for i in list(line)] for line in problem_input.splitlines()])
    # print("Before any steps:")
    octopuses.print_map()
    if level == 1:
        for i in range(100):
            # print("After step " + str(i + 1))
            octopuses.step()
            octopuses.print_map()
        return octopuses.flashes
    else:
        step_count = 1
        while True:
            octopuses.step()
            if octopuses.count_lights() == 100:
                return step_count
            else:
                step_count += 1


aoc_utils.run(answer, cases)
