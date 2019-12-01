from aoc_utils import aoc_utils
import os


def determine_fuel(mass):
    return int(int(mass) / 3) - 2

def determine_fuel_amended(mass):
    continuous_mass = 0

    while True:
        mass = determine_fuel(mass)
        if mass < 0:
            return continuous_mass
        continuous_mass += mass


def answer(problem_input, level):
    total_fuel_requirement = 0

    for mass in problem_input.splitlines():
        if level == 1:
            total_fuel_requirement += determine_fuel(mass)
        elif level == 2:
            total_fuel_requirement += determine_fuel_amended(mass)

    return total_fuel_requirement


test_cases = [
    {'level': 1, 'input': '12', 'output': '2'},
    {'level': 1, 'input': '14', 'output': '2'},
    {'level': 1, 'input': '1969', 'output': '654'},
    {'level': 1, 'input': '100756', 'output': '33583'},
    {'level': 2, 'input': '14', 'output': '2'},
    {'level': 2, 'input': '1969', 'output': '966'},
    {'level': 2, 'input': '100756', 'output': '50346'}
]

problem_input = aoc_utils.fetch_and_save()
aoc_utils.test_and_submit(test_cases, problem_input, answer)
