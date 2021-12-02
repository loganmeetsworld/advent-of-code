from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in problem_input.splitlines():
        command, amount = [i[0:-2], int(i[-1])]
        if command == 'forward':
            horizontal_pos += amount
            if level == 2:
                depth += (aim * amount)
        elif command == 'down':
            if level == 1:
                depth += amount
            aim += amount
        elif command == 'up':
            if level == 1:
                depth -= amount
            aim -= amount

    return horizontal_pos * depth


aoc_utils.run(answer, cases)
