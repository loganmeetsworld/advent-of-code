import re

from aoc_utils import aoc_utils
from tests import cases


def create_stacks(crane_map):
    places = [1]
    while len(crane_map[0]) > places[-1] + 4:
        places.append(places[-1] + 4)
    cranes = []
    for crane in crane_map:
        crane_row = []
        for place in places:
            crane_row.append(crane[place])
        cranes.append(crane_row)
    rows, columns = len(cranes), len(cranes[0])
    stacks = []
    for j in range(columns):
        row = []
        for i in range(rows):
            if cranes[i][j] != " ":
                row.append(cranes[i][j])
        stacks.append(row)
    return stacks


def answer(problem_input, level, test=False):
    crane_map, directions = problem_input.split('\n\n')
    directions = directions.splitlines()
    stacks =  create_stacks(crane_map.splitlines()[:-1])
    for direction in directions:
        num_to_move, from_idx, to_idx = re.findall("(\d+)", direction)
        if level == 1:
            for _ in range(int(num_to_move)):
                pop = stacks[int(from_idx) - 1].pop(0)
                stacks[int(to_idx) - 1].insert(0, pop)
        elif level == 2:
            popped = stacks[int(from_idx ) - 1][0:int(num_to_move)]
            for _ in range(int(num_to_move)):
                stacks[int(from_idx) - 1].pop(0)
            stacks[int(to_idx) - 1] = popped + stacks[int(to_idx) - 1]

    return "".join([crane[0] for crane in stacks])


aoc_utils.run(answer, cases)
