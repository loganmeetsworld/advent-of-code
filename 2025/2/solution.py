from aoc_utils import aoc_utils
from tests import cases

def id_has_double_pattern(id):
    return id[:len(id)//2] == id[len(id)//2:]

def check_for_invalid_ids_part_1(id_range):
    invalid_ids = []
    start_range, end_range = id_range.split('-')
    for id in range(int(start_range), int(end_range) + 1):
        if id_has_double_pattern(str(id)):
            invalid_ids.append(id)

    return invalid_ids

def answer(problem_input, level, test=False):
    id_ranges = problem_input.split(",")
    invalid_ids = []
    for id_range in id_ranges:
        if level == 1:
            invalid_ids += check_for_invalid_ids_part_1(id_range)
    return sum(invalid_ids)

aoc_utils.run(answer, cases)
