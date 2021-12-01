from aoc_utils import aoc_utils
from tests import cases

def count_increased(l):
    increased_count = 0
    for idx in range(1, len(l)):
        if l[idx] - l[idx - 1] > 0:
            increased_count += 1
    return increased_count


def get_triplet_sums(depths):
    triplet_sums = []
    start_range = 0
    end_range = 2
    while end_range < len(depths):
        triplet_sums.append(sum(depths[start_range:end_range + 1]))
        start_range += 1
        end_range += 1
    return triplet_sums


def answer(problem_input, level, test=False):
    depths = [int(i) for i in problem_input.splitlines()]

    if level == 1:
        return count_increased(depths)
    elif level == 2:
        triplets = get_triplet_sums(depths)
        return count_increased(triplets)


aoc_utils.run(answer, cases)
