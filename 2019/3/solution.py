import json

from aoc_utils import aoc_utils
from tests import cases


def travel(wire):
    instructions = wire.split(',')
    steps = 0
    location = [0, 0]
    locations_traveled = {}

    for instruction in instructions:
        direction, length = instruction[0], int(instruction[1:])
        # print(f'{direction}: {length}')
        if direction == 'R':
            for i in range(1, length + 1):
                steps += 1
                locations_traveled[str([location[0] + i, location[1]])] = steps
                # print(f'{[location[0] + i, location[1]]}: {steps}')
            location[0] += i
        elif direction == 'L':
            for i in range(1, length + 1):
                steps += 1
                locations_traveled[str([location[0] - i, location[1]])] = steps
                # print(f'{[location[0] - i, location[1]]}: {steps}')
            location[0] -= i
        elif direction == 'U':
            for i in range(1, length + 1):
                steps += 1
                locations_traveled[str([location[0], location[1] + i])] = steps
                # print(f'{[location[0], location[1] + i]}: {steps}')
            location[1] += i
        elif direction == 'D':
            for i in range(1, length + 1):
                steps += 1
                locations_traveled[str([location[0], location[1] - i])] = steps
                # print(f'{[location[0], location[1] - i]}: {steps}')
            location[1] -= i

    return locations_traveled


def find_shortest_distance_to_intersection(locations_1, locations_2):
    distances_1 = [json.loads(key) for key in list(locations_1.keys())]
    distances_2 = [json.loads(key) for key in list(locations_2.keys())]
    intersections = [json.loads(l) for l in list(set([str(a) for a in distances_1]).intersection([str(b) for b in distances_2]))]

    # Find the intersection with the smallest distance
    shortest_distance = min([abs(x[0]) + abs(x[1]) for x in intersections])
    shortest_distance_coords = [y for y in intersections if abs(y[0]) + abs(y[1]) == shortest_distance][0]
    print(shortest_distance_coords)
    steps = locations_1[str(shortest_distance_coords)] + locations_2[str(shortest_distance_coords)]

    return [shortest_distance, steps]


def answer(problem_input, level, test=False):
    wire_1, wire_2 = problem_input.split("\n")
    locations_1, locations_2 = travel(wire_1), travel(wire_2)
    distance, steps = find_shortest_distance_to_intersection(locations_1, locations_2)
    return distance if level == 1 else steps


aoc_utils.run(answer, cases)
