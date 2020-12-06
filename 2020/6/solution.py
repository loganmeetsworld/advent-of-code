from collections import Counter

from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    if level == 1:
        return sum([len(set(group.replace('\n', ''))) for group in problem_input.split('\n\n')])
    elif level == 2:
        counts = 0
        for group in problem_input.split('\n\n'):
            counter = Counter()
            [counter.update(elf) for elf in group.splitlines()]
            for _, v in counter.items():
                if v / len(group.splitlines()) == 1:
                    counts += 1

        return counts


aoc_utils.run(answer, cases)
