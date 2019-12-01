import sys
sys.path.append('../../')
from aoc_automation import problem_input, submit
import os

def calculate_weight(weight):
    return int(int(weight) / 3) - 2


def continuous_calc_weight(weight):
    total_weight = 0

    while int(weight) > 0:
        weight = calculate_weight(weight)
        if weight < 0:
            return total_weight
        total_weight += weight
    
    return total_weight


def day_1(problem_input):
    total_weight = 0

    for weight in problem_input:
        total_weight += calculate_weight(weight)
    
    return total_weight


def day_2(problem_input):
    total_weight = 0

    for weight in problem_input:
        total_weight += continuous_calc_weight(weight)

    return total_weight


problem_path = os.path.abspath(__file__)
problem_input = problem_input(problem_path).splitlines()
submit(problem_path, "1", day_1(problem_input))
submit(problem_path, "2", day_2(problem_input))
