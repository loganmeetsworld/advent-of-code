import copy

from aoc_utils import aoc_utils
from tests import cases


def calculate_bus_departure(earliest_departure, schedule):
    ed = copy.copy(earliest_departure)
    while True:
        ed += 1
        for bus in schedule:
            if ed % bus == 0:
                return bus * (ed - earliest_departure)
                break


def calculate_cascading_bus_minutes(schedule):
    return 0


def answer(problem_input, level, test=False):
    earliest_departure, schedule = problem_input.splitlines()
    schedule = [int(i) for i in schedule.replace('x', '').split(',') if i]
    if level == 1:
        return calculate_bus_departure(int(earliest_departure), schedule)
    else:
        return calculate_cascading_bus_minutes(schedule)


aoc_utils.run(answer, cases)
