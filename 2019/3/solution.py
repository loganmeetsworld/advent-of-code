import json

from aoc_utils import aoc_utils
from tests import cases


def travel(wire):
    locations_traveled = []
    location = [0, 0]
    for pos in wire:
        direction, distance = pos[0], int(pos[1:])
        for _ in range(distance):
            if direction == 'R':
                location[0] += 1
            elif direction == 'L':
                location[0] -= 1
            elif direction == 'U':
                location[1] += 1
            elif direction == 'D':
                location[1] -= 1
            locations_traveled.append([location[0], location[1]])
    return locations_traveled


def find_shortest_distance_to_intersection(locations_1, locations_2):
    intersections = [json.loads(j) for j in set([str(i) for i in locations_1]).intersection([str(i) for i in locations_2])]
    shortest_distance = min(abs(i[0]) + abs(i[1]) for i in intersections)
    steps = min([locations_1.index(i) + locations_2.index(i) for i in intersections])
    return [shortest_distance, steps + 2]


def answer(problem_input, level, test=False):
    wire_1, wire_2 = problem_input.split("\n")
    locations_1, locations_2 = travel(wire_1.split(',')), travel(wire_2.split(','))
    distance, steps = find_shortest_distance_to_intersection(locations_1, locations_2)
    return distance if level == 1 else steps


aoc_utils.run(answer, cases)
