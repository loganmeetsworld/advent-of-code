import copy
from math import gcd

from aoc_utils import aoc_utils
from tests import cases


def least_common_multiple(a, b):
    # https://www.w3schools.com/python/ref_math_gcd.asp
    return a * b // gcd(a, b)


def calculate_bus_departure(earliest_departure, schedule):
    ed = copy.copy(earliest_departure)
    while True:
        ed += 1
        for bus in schedule:
            if ed % bus == 0:
                return bus * (ed - earliest_departure)
                break


def calculate_cascading_bus_minutes(schedule):
    position, bus_number = schedule[0]
    for next_position, next_bus_number in schedule[1:]:
        while True:
            position += bus_number
            if (position + next_position) % next_bus_number == 0:
                break

        bus_number = least_common_multiple(bus_number, next_bus_number)

    return position


def answer(problem_input, level, test=False):
    earliest_departure, schedule = problem_input.splitlines()
    if level == 1:
        schedule = [int(bus) for bus in schedule.replace('x', '').split(',') if bus]
        return calculate_bus_departure(int(earliest_departure), schedule)
    else:
        schedule = [[i, int(bus)] for i, bus in enumerate(schedule.split(',')) if bus != 'x']
        return calculate_cascading_bus_minutes(schedule)


aoc_utils.run(answer, cases)
