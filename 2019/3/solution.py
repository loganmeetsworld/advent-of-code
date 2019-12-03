from aoc_utils import aoc_utils
from tests import cases

WIRES_START_POINT = [0, 0]


def travel(wire):
    print('\n')
    location = WIRES_START_POINT
    locations_traveled = []
    instructions = wire.split(',')
    for instr in instructions:
        direction = instr[0]
        length = int(instr[1])
        if direction == 'R':
            location[0] += length
            new_location_set = []
            for i in range(length):
                new_location_set.append([i, location[1]])
            print(new_location_set)
            locations_traveled.append(new_location_set)
        elif direction == 'L':
            location[0] -= length
            new_location_set = []
            for i in range(length):
                new_location_set.append([i, location[1]])
            print(new_location_set)
            locations_traveled.append(new_location_set)
        elif direction == 'U':
            location[1] += length
            new_location_set = []
            for i in range(length):
                new_location_set.append([location[0], i])
            print(new_location_set)
            locations_traveled.append(new_location_set)
        elif direction == 'D':
            location[1] -= length
            new_location_set = []
            for i in range(length):
                new_location_set.append([location[0], i])
            print(new_location_set)
            locations_traveled.append(new_location_set)
    return locations_traveled


def manhattan_distance(arr_1, arr_2):
    WIRES_START_POINT


def answer(problem_input, part, test=False):
    wire_1, wire_2 = problem_input.split("\n")
    wire_1_locations_visited = travel(wire_1)
    wire_2_locations_visited = travel(wire_2)
    
    return manhattan_distance(wire_1_locations_visited, wire_2_locations_visited)


aoc_utils.run(answer, cases)