from collections import defaultdict
import re

from aoc_utils import aoc_utils
from tests import cases

PARENT_BAG_REGEX = r'^(\w+ \w+)'
CHILD_BAG_REGEX = r'(\d+) (\w+ \w+)'
MY_BAG = 'shiny gold'


def bag_possibilities(bag, bag_count_map):
    for inner_bag in bag:
        bag = set(bag) | bag_possibilities(bag_count_map[inner_bag], bag_count_map)

    return set(bag)


def count_bags_in_bags(bag, bag_size_map):
    count = 0
    for num_bags, bname in bag_size_map[bag]:
        count += int(num_bags) * count_bags_in_bags(bname, bag_size_map)

    return count + 1


def answer(problem_input, level, test=False):
    bag_count_map = defaultdict(list)
    bag_size_map = {}
    for line in problem_input.splitlines():
        parent_bag = re.search(PARENT_BAG_REGEX, line)[0]
        child_bags = re.findall(CHILD_BAG_REGEX, line)
        bag_size_map[parent_bag] = child_bags
        for bag in child_bags:
            bag_count_map[bag[1]].append(parent_bag)

    if level == 1:
        return len(bag_possibilities(bag_count_map[MY_BAG], bag_count_map))
    else:
        return count_bags_in_bags(MY_BAG, bag_size_map) - 1


aoc_utils.run(answer, cases)
