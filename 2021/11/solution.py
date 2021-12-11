from aoc_utils import aoc_utils
from tests import cases
   

class OctopusEnergyMap():
    def __init__(self, omap):
        self.map = omap
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.burnouts = []
        self.flashes = 0
        self.step_count = 0

    def step(self):
        self.step_count += 1
        for ypos, y in enumerate(self.map):
            for xpos, _ in enumerate(y):
                self.energy_gain(ypos, xpos)
        self.refresh_octos()

    def energy_gain(self, ypos, xpos):
        if ypos < 0 or ypos >= self.height or xpos < 0 or xpos >= self.width: return
        self.map[ypos][xpos] += 1
        if self.map[ypos][xpos] == 10:
            self.flash(ypos, xpos)

    def flash(self, ypos, xpos):
        self.flashes += 1
        self.burnouts.append([ypos, xpos])
        [self.energy_gain(*n) for n in self.get_neighbors(ypos, xpos)]

    def refresh_octos(self):
        for ypos, xpos in self.burnouts:
            self.map[ypos][xpos] = 0
        self.burnouts = []
        
    def count_lights(self):
        return sum([l.count(0) for l in self.map])

    def print_map(self):
        [print("".join(['\033[1m' + str(i) + '\033[0m' if i == 0 else str(i) for i in line])) for line in self.map]
        print()

    @staticmethod 
    def get_neighbors(ypos, xpos):
        return [            
            [ypos, xpos - 1],
            [ypos, xpos + 1],
            [ypos - 1, xpos],
            [ypos + 1, xpos],
            [ypos - 1, xpos - 1],
            [ypos + 1, xpos + 1],
            [ypos - 1, xpos + 1],
            [ypos + 1, xpos - 1]
        ]

def answer(problem_input, level, test=False):
    octopuses = OctopusEnergyMap([[int(i) for i in list(line)] for line in problem_input.splitlines()])
    steps = 100

    if level == 1:
        for _ in range(steps):
            octopuses.step()
            # octopuses.print_map()
        return octopuses.flashes
    elif level == 2:
        while True:
            octopuses.step()
            # octopuses.print_map()
            if octopuses.count_lights() == 100: return octopuses.step_count


aoc_utils.run(answer, cases)
