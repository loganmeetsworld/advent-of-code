from aoc_utils import aoc_utils

def calculate_weight(weight):
    return int(int(weight) / 3) - 2

def continuous_calc_weight(weight):
    continuous_weight = 0

    while True:
        weight = calculate_weight(weight)
        if weight < 0:
            return continuous_weight
        continuous_weight += weight


def answer(problem_input, level):
    total_weight = 0

    for weight in problem_input:
        if level == 1:
            total_weight += calculate_weight(weight)
        else:
            total_weight += continuous_calc_weight(weight)

    return total_weight

problem_input = aoc_utils.fetch(2019, 1, 'input').splitlines()
print(aoc_utils.fetch(2019, 1, 'problem'))

test_cases = [
    {'level': 1, 'input': ['12'], 'output': '2'},
    {'level': 1, 'input': ['14'], 'output': '2'},
    {'level': 1, 'input': ['1969'], 'output': '654'},
    {'level': 1, 'input': ['100756'], 'output': '33583'},
    {'level': 2, 'input': ['14'], 'output': '2'},
    {'level': 2, 'input': ['1969'], 'output': '966'},
    {'level': 2, 'input': ['100756'], 'output': '50346'}
]
aoc_utils.test_and_submit(2019, 1, test_cases, problem_input, answer)
