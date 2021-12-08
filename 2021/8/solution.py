from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    outputs, acceptible_lengths = [], [2, 3, 4, 7]
    for line in problem_input.splitlines():
        outputs += line.split(' | ')[1].split()
    return sum(1 for i in outputs if len(i) in acceptible_lengths)


aoc_utils.run(answer, cases)
