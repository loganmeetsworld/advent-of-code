from aoc_utils import aoc_utils
import os

def answer(problem_input, part):
    print(problem_input)

path = os.path.abspath(__file__)
problem_input = aoc_utils.fetch(path, 'input')
print(aoc_utils.fetch(path, 'problem'))

# part, input, correct answer
test_cases = [
    [1, '', ''],
    [1, '', ''],
    [1, '', ''],
]

aoc_utils.test_and_submit(path, test_cases, problem_input, answer)
