from aoc_utils import aoc_utils
from tests import cases


def determine_fuel(mass):
    return int(mass / 3) - 2


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
            total_fuel_requirement += determine_fuel(int(mass))
        elif level == 2:
            total_fuel_requirement += determine_fuel_amended(int(mass))
    return total_fuel_requirement


problem_input = aoc_utils.fetch_and_save()
aoc_utils.test_and_submit(cases, problem_input, answer)
