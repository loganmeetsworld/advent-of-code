from collections import defaultdict
import re

from aoc_utils import aoc_utils
from tests import cases

PARENT_BAG_REGEX = r'^(\w+ \w+)'
CHILD_BAG_REGEX = r'\d+ (\w+ \w+)'
MY_BAG = 'shiny gold'


def count_bags(bag, bag_map):
    for inner_bag in bag:
        bag = set(bag) | count_bags(bag_map[inner_bag], bag_map)

    return set(bag)


def answer(problem_input, level, test=False):
    bag_map = defaultdict(list)
    for line in problem_input.splitlines():
        parent_bag = re.search(PARENT_BAG_REGEX, line).group(1)
        for bag in re.findall(CHILD_BAG_REGEX, line):
            bag_map[bag].append(parent_bag)

    return len(count_bags(bag_map[MY_BAG], bag_map))


aoc_utils.run(answer, cases)
