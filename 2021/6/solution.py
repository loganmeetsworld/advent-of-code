from aoc_utils import aoc_utils
from tests import cases


class Lanternfish():
    def __init__(self, birth_cycle):
        self.birth_cycle = birth_cycle
    def grow(self):
        self.birth_cycle -= 1
    def birth(self):
        self.birth_cycle = 7
    def pregnant(self):
        return self.birth_cycle == 0


def answer(problem_input, level, test=False):
    if level == 1:
        days = 80
    elif level == 2:
        days = 256
    
    fishies = [Lanternfish(int(i)) for i in problem_input.split(',')]

    while days > 0:
        for fish in fishies:
            if fish.pregnant():
                fishies.append(Lanternfish(9))
                fish.birth()
            fish.grow()
        days -= 1
    
    return len(fishies)


aoc_utils.run(answer, cases)
