from aoc_utils import aoc_utils
import os

def calculate_weight(weight):
    return int(int(weight) / 3) - 2

def continuous_calc_weight(weight):
    continuous_weight = 0

    while int(weight) > 0:
        weight = calculate_weight(weight)
        if weight < 0:
            return continuous_weight
        continuous_weight += weight
    
    return continuous_weight

def answer(problem_input, part):
    total_weight = 0

    if part == 1:
        for weight in problem_input:
            total_weight += calculate_weight(weight)
    else:
        for weight in problem_input:
            total_weight += continuous_calc_weight(weight)

    return total_weight

path = os.path.abspath(__file__)
problem_input = aoc_utils.fetch(path, 'input').splitlines()
test_cases = [
    [1, ['12'], '2'],
    [1, ['14'], '2'],
    [1, ['1969'], '654'],
    [1, ['100756'], '33583'],
    [2, ['14'], '2'],
    [2, ['1969'], '966'],
    [2, ['100756'], '50346']
]
aoc_utils.test_and_submit(path, test_cases, problem_input, answer)
