import copy

from aoc_utils import aoc_utils
from tests import cases


def bus_arriving(ed, schedule):
    for bus in schedule:
        if ed % bus == 0:
            return bus


def calculate_bus_departure(earliest_departure, schedule):
    ed = copy.copy(earliest_departure)
    while True:
        ed += 1
        if ed == 100:
            break
        bus = bus_arriving(ed, schedule)
        if bus:
            return bus * (ed - earliest_departure)
            break


def answer(problem_input, level, test=False):
    earliest_departure, schedule = problem_input.splitlines()
    schedule = [int(i) for i in schedule.replace('x', '').split(',') if i]
    bus_departure = calculate_bus_departure(int(earliest_departure), schedule)
    return bus_departure


aoc_utils.run(answer, cases)
