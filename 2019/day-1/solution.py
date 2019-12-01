import sys
sys.path.append('../../')
from aoc_automation import problem_input, submit
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


problem_path = os.path.abspath(__file__)
problem_input = problem_input(problem_path).splitlines()
submit(problem_path, 1, answer(problem_input, 1))
submit(problem_path, 2, answer(problem_input, 2))
