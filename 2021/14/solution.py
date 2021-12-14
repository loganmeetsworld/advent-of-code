import re

from collections import Counter, defaultdict

from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    steps = 10 if level == 1 else 40
    polymer, rules = problem_input.split("\n\n")

    # Create a dictionary to hold the rules {'NN': 'C'}
    rules_hash = {}
    for r in rules.splitlines():
        k, v = r.split(' -> ')
        rules_hash[k] = v

    # Create a dictionary with pairs and their counts
    pairs = defaultdict(int)
    for idx, _ in enumerate(polymer):
        if len(polymer[idx:idx+2]) == 1:
            continue
        pairs[polymer[idx:idx+2]] = 1
    
    # Create a counter for each letter
    letter_counts = Counter(polymer)

    # Do each step
    for _ in range(steps):
        # For each round, take all current pairs and their counts
        for pair, count in pairs.items():
            pairs = pairs.copy()
            # Get injection letter from the rules
            letter = rules_hash[pair]
            # Decrease the count of the original pair
            # and increase the count of the replacement pairs
            # ex AB -> C suggests new pairs AC and CB
            pairs[pair] -= count
            pairs[pair[0] + letter] += count
            pairs[letter + pair[1]] += count
            # Increase the count of the letter
            letter_counts[letter] += count

    counter = letter_counts.values()
    return max(counter) - min(counter)


aoc_utils.run(answer, cases)
