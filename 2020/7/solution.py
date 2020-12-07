from collections import defaultdict
import re

from aoc_utils import aoc_utils
from tests import cases

PARENT_BAG_REGEX = r'^(\w+ \w+)'
BAG_COUNT_REGEX = r'(\d+) (\w+ \w+)'
MY_BAG = 'shiny gold'


def find_inner_bags(bag, bag_count_map):
    for inner_bag in bag:
        bag = set(bag) | find_inner_bags(bag_count_map[inner_bag], bag_count_map)

    return set(bag)


def find_bag_mandate(bag, bag_size_map):
    count = 0
    for inner_bag in bag:
        print(inner_bag)
        print(bag_size_map)
        count += int(inner_bag[0])
        find_bag_mandate(bag_size_map[inner_bag[1]], bag_size_map)

    return count


def answer(problem_input, level, test=False):
    bag_count_map = defaultdict(list)
    bag_size_map = {}
    for line in problem_input.splitlines():
        parent_bag = re.search(PARENT_BAG_REGEX, line).group(1)
        child_bags = re.findall(BAG_COUNT_REGEX, line)
        bag_size_map[parent_bag] = child_bags
        for bag in child_bags:
            bag_count_map[bag[1]].append(parent_bag)

    if level == 1:
        return len(find_inner_bags(bag_count_map[MY_BAG], bag_count_map))
    else:
        return find_bag_mandate(bag_size_map[MY_BAG], bag_size_map)


aoc_utils.run(answer, cases)
