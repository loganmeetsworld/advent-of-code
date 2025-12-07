from aoc_utils import aoc_utils
from tests import cases

import re
import math

def answer(problem_input, level, test=False):
    if level == 1:
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
    elif level == 2:
        rows = problem_input.splitlines()
        all_chars = []
        total = 0
        for y in range(len(rows[0]) - 1, -1, -1):
            chars = "".join([x[y] for x in rows]).strip()
            if chars == "":
                continue
            if "+" not in chars and "*" not in chars:
                all_chars.append(chars)
            else:
                all_chars.append(chars[0:-1])
                if "+" in chars:
                    total += sum([int(i) for i in all_chars])
                if "*" in chars:
                    total += math.prod([int(i) for i in all_chars])
                all_chars = []
        
        return total

aoc_utils.run(answer, cases)
