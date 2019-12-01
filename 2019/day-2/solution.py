from aoc_utils import aoc_utils

def answer(problem_input, part):
    print(problem_input)

problem_input = aoc_utils.fetch(2019, 2, 'input')
print(aoc_utils.fetch(2019, 2, 'problem'))

# part, input, correct answer
test_cases = [
    [1, '', ''],
    [1, '', ''],
    [1, '', ''],
]

aoc_utils.test_and_submit(2019, 2, test_cases, problem_input, answer)
