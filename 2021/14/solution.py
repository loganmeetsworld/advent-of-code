import re

from collections import Counter

from aoc_utils import aoc_utils
from tests import cases


def transform(polymer, rules_hash):
    idx = 0
    while idx < len(polymer):
        next_phrase = polymer[idx:idx+2]
        if ''.join(next_phrase) in rules_hash.keys():
            polymer.insert(idx+1, rules_hash[''.join(next_phrase)])
            idx += 2
        else:
            idx += 1

    return polymer


def answer(problem_input, level, test=False):
    steps = 10
    polymer, rules = problem_input.split("\n\n")
    rules_hash = {}
    for r in rules.splitlines():
        k, v = r.split(' -> ')
        rules_hash[k] = v

    for _ in range(steps):
        polymer = transform(list(polymer), rules_hash)

    counter = Counter(polymer).values()
    return max(counter) - min(counter)


aoc_utils.run(answer, cases)
