from collections import defaultdict
import re

from aoc_utils import aoc_utils
from tests import cases


def find_bag_locations(inner_bag_map, bname):
    bag = inner_bag_map[bname]
    for inner_bag in bag:
        bag = set(bag) | find_bag_locations(inner_bag_map, inner_bag)
    return set(bag)


def find_bags_in_bag(bag_size_map, bag):
    count = 1
    for num_bags, bname in bag_size_map[bag]:
        count += int(num_bags) * find_bags_in_bag(bag_size_map, bname)
    return count


def answer(problem_input, level, test=False):
    inner_bag_map = defaultdict(list)
    bag_size_map = {}
    for line in problem_input.splitlines():
        parent_bag, child_bags = re.search(r'^(\w+ \w+)', line)[0], re.findall(r'(\d+) (\w+ \w+)', line)
        bag_size_map[parent_bag] = child_bags
        for bag in child_bags:
            inner_bag_map[bag[1]].append(parent_bag)

    return len(find_bag_locations(inner_bag_map, 'shiny gold')) if level == 1 else find_bags_in_bag(bag_size_map, 'shiny gold') - 1


aoc_utils.run(answer, cases)
