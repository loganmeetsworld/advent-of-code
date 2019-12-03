import json

from aoc_utils import aoc_utils
from tests import cases


def travel(wire):
    instructions = wire.split(',')
    locations_traveled = [[0, 0]]

    for instruction in instructions:
        direction, length = instruction[0], int(instruction[1:])
        for i in range(length):
            location = locations_traveled[-1]
            if direction == 'R':
                location[0] += 1
            elif direction == 'L':
                location[0] -= i
            elif direction == 'U':
                location[1] += i
            elif direction == 'D':
                location[1] -= i

            locations_traveled.append(location)

    return locations_traveled


def find_shortest_distance_to_intersection(locations_1, locations_2):
    intersections = set([str(a) for a in locations_1]).intersection([str(b) for b in locations_2])
    intersections = [json.loads(i) for i in intersections]
    intersections.remove([0, 0])
    shortest_distance = min(intersections[1:], key=lambda p: abs(p[0]) + abs(p[1]))

    steps = [locations_1.index(p) + locations_2.index(p) for p in intersections]

    return [shortest_distance, steps]


def answer(problem_input, level, test=False):
    wire_1, wire_2 = problem_input.split("\n")
    locations_1, locations_2 = travel(wire_1), travel(wire_2)
    distance, steps = find_shortest_distance_to_intersection(locations_1, locations_2)
    return distance if level == 1 else steps


aoc_utils.run(answer, cases)
