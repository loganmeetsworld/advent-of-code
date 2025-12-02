from aoc_utils import aoc_utils
from tests import cases
import math

def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def id_is_all_repeats(id):
    max_chunk = math.ceil(len(id) / 2)
    for n in range(1,max_chunk+1):
        chunks = chunk_list(id, n)
        if len(set(chunks)) == 1:
            return True  
    return False

def id_has_double_pattern(id):
    return id[:len(id)//2] == id[len(id)//2:]

def check_for_invalid_ids(id_range, level):
    invalid_ids = []
    start_range, end_range = id_range.split('-')
    for id in range(int(start_range), int(end_range) + 1):
        if level == 1:
            if id_has_double_pattern(str(id)):
                invalid_ids.append(id)
        if level == 2:
            if len(str(id)) > 1 and id_is_all_repeats(str(id)):
                invalid_ids.append(id)

    return invalid_ids

def answer(problem_input, level, test=False):
    id_ranges = problem_input.split(",")
    invalid_ids = []
    for id_range in id_ranges:
        invalid_ids += check_for_invalid_ids(id_range, level)
    return sum(invalid_ids)

aoc_utils.run(answer, cases)
