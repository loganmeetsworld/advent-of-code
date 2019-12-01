from aoc_utils import aoc_utils

def answer(problem_input, part):
    return 0

test_cases = [
    {'level': 1, 'input': "1,-1,-1,-2\n-2,-2,0,1\n0,2,1,3\n-2,3,-2,1\n0,2,3,-2\n-1,-1,1,-2\n0,-2,-1,0\n-2,2,3,-1\n1,2,2,0\n-1,-2,0,-2", 'output': '8'},
]
problem_input = aoc_utils.fetch_and_save()
aoc_utils.test_and_submit(test_cases, problem_input, answer)
    