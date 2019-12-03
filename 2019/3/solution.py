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
        if direction == 'R':
            for i in range(length + 1):
                steps += 1
                locations_traveled[str([location[0] + i, location[1]])] = steps
            location[0] += i
        elif direction == 'L':
            for i in range(length + 1):
                steps += 1
                locations_traveled[str([location[0] - i, location[1]])] = steps
            location[0] -= i
        elif direction == 'U':
            for i in range(length + 1):
                steps += 1
                locations_traveled[str([location[0], location[1] + i])] = steps
            location[1] += i
        elif direction == 'D':
            for i in range(length + 1):
                steps += 1
                locations_traveled[str([location[0], location[1] - i])] = steps
            location[1] -= i

    return locations_traveled


def find_shortest_distance_to_intersection(locations_1, locations_2):
    distances_1 = [json.loads(key) for key in list(locations_1.keys())]
    distances_2 = [json.loads(key) for key in list(locations_2.keys())]

    intersections = [json.loads(l) for l in list(set([str(a) for a in distances_1]).intersection([str(b) for b in distances_2]))]
    intersections.remove([0, 0])
    distance_values = []
    for d in intersections:
        # print(locations_1)
        # print(intersections)
        # print([json.loads(list(d.keys())[0]) for d in locations_1])
        steps_1 = [list(a.values())[0] for a in locations_1 if json.loads(list(a.keys())[0]) == d]
        steps_2 = [list(a.values())[0] for a in locations_2 if json.loads(list(a.keys())[0]) == d]
        combined_steps = int(steps_1[0]) + int(steps_2[0])
        distance_values.append([abs(d[0]) + abs(d[1]), combined_steps])
        print(combined_steps)
        print(distance_values)

    distance_calcs = [d[0] for d in distance_values]
    [d for d in distance_values if d[0] == min(distance_calcs)]

    return [d for d in distance_values if d[0] == min(distance_calcs)]


def answer(problem_input, level, test=False):
    wire_1, wire_2 = problem_input.split("\n")
    locations_1, locations_2 = travel(wire_1), travel(wire_2)
    distance, steps = find_shortest_distance_to_intersection(locations_1, locations_2)
    return distance if level == 1 else steps


aoc_utils.run(answer, cases)
