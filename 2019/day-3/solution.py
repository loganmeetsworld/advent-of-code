from aoc_utils import aoc_utils
import os

def answer(problem_input, part):
    print(problem_input)

test_cases = [
    {'level': 1, 'input': '', 'output': ''},
    {'level': 1, 'input': '', 'output': ''},
    {'level': 1, 'input': '', 'output': ''},
]

year, day = aoc_utils.detect_time()
problem_input = aoc_utils.fetch_and_save(year, day)
aoc_utils.test_and_submit(year, day, test_cases, problem_input, answer)
    