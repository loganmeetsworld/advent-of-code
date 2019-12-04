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


def find_shortest_distance_to_intersection(l1, l2):
    intersections = set([str(i) for i in l1]).intersection([str(i) for i in l2])
    intersections = [json.loads(i) for i in intersections]
    shortest_distance = min(sum(i) for i in intersections)
    steps = [l1.index(p) + l2.index(p) for p in intersections]

    return [shortest_distance, sum(steps)]


def answer(problem_input, level, test=False):
    wire_1, wire_2 = problem_input.split("\n")
    l1, l2 = travel(wire_1.split(',')), travel(wire_2.split(','))
    distance, steps = find_shortest_distance_to_intersection(l1, l2)
    return distance if level == 1 else steps


aoc_utils.run(answer, cases)
