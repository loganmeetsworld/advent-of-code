from aoc_utils import aoc_utils
from tests import cases

WIRES_START_POINT = [0, 0]


def travel(wire):
    location = WIRES_START_POINT
    locations_traveled = []
    instructions = wire.split(',')
    for instr in instructions:
        direction = instr[0]
        length = int(instr[1:])
        if direction == 'R':
            for i in range(length):
                new_x = location[0] + i
                locations_traveled.append([new_x, location[1]])
            location = [new_x + 1, location[1]]
            locations_traveled.append(location)
        elif direction == 'L':
            for i in range(length):
                new_x = location[0] - i
                locations_traveled.append([new_x, location[1]])
            location = [new_x - 1, location[1]]
            locations_traveled.append(location)
        elif direction == 'U':
            for i in range(length):
                new_y = location[1] + i
                locations_traveled.append([location[0], new_y])
            location = [location[0], new_y + 1]
            locations_traveled.append(location)
        elif direction == 'D':
            for i in range(length):
                new_y = location[1] - i
                locations_traveled.append([location[0], new_y])
            location = [location[0], new_y - 1]
            locations_traveled.append(location)
    locations_traveled.remove([0, 0])
    # print(locations_traveled)
    return locations_traveled


def manhattan_distances(arr_1, arr_2):
    import json
    string_set = list(set([str(a) for a in arr_1]).intersection([str(b) for b in arr_2]))
    distances = [json.loads(l) for l in string_set]
    bleh = []
    for d in distances:
        bleh.append(abs(d[0]) + abs(d[1]))
    print(distances)
    return bleh


def answer(problem_input, part, test=False):
    wire_1, wire_2 = problem_input.split("\n")
    wire_1_locations_visited = travel(wire_1)
    wire_2_locations_visited = travel(wire_2)

    distances = manhattan_distances(wire_1_locations_visited, wire_2_locations_visited)

    return min(distances)


aoc_utils.run(answer, cases)