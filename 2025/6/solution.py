from aoc_utils import aoc_utils
from tests import cases

import re
import math

def answer(problem_input, level, test=False):
    numbers = [re.findall(r'\d+', l) for l in problem_input.splitlines()[0:-1]]
    operations = [i.split() for i in problem_input.splitlines()[-1].replace(" ", "")]
    total_nums = []
    for y in range(len(numbers[0])):
        collected_nums = []
        for x in range(len(numbers)):
            collected_nums.append(int(numbers[x][y]))
        operation = operations[y]
        if operation[0] == "*":
            total_nums.append(math.prod(collected_nums))
        elif operation[0] == "+":
            total_nums.append(sum(collected_nums))
    return sum(total_nums)


aoc_utils.run(answer, cases)
