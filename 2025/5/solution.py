from aoc_utils import aoc_utils
from tests import cases

def merge_ranges(ranges):
    merged_ranges = []
    for start, end in sorted(ranges):
        if not merged_ranges or start > merged_ranges[-1][1]:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
    return merged_ranges


def answer(problem_input, level, test=False):
    ingredient_id_ranges, ingredient_ids = problem_input.split("\n\n")
    ingredient_ids = [int(i) for i in ingredient_ids.splitlines()]
    ingredient_id_ranges_list = []
    for ingredient_id_range in ingredient_id_ranges.splitlines():
        first, last = ingredient_id_range.split('-')
        ingredient_id_ranges_list.append((int(first), int(last)))

    if level == 1:
        fresh_id_count = 0
        for ingredient in ingredient_ids:
            found_in_range = False
            for first, last in ingredient_id_ranges_list:
                if first <= ingredient <= last:
                    # Save some time by breaking early if we find it
                    found_in_range = True
                    break
            if found_in_range:
                fresh_id_count += 1

        return fresh_id_count
    elif level == 2:
        fresh_id_count = 0
        consolidated_ranges = merge_ranges(ingredient_id_ranges_list)
        for first, last in consolidated_ranges:
            fresh_id_count += 1
            fresh_id_count += (last-first)

        return fresh_id_count


aoc_utils.run(answer, cases)
