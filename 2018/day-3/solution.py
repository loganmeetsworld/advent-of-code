import re

print("Part 1:")
lines = open('input.txt', 'r').read().strip().splitlines()
square_dimension = 10


def build_square(dim):
    return [['.'] * dim] * dim


def parse(line):
    scan = re.findall(r'\d+', line)
    return {'id': scan[0], 'dist_from_left': int(scan[1]), 'dist_from_top': int(scan[2]), 'width': int(scan[3]), 'height': int(scan[4])}


square = build_square(square_dimension)
claims = [parse(x) for x in lines]

for claim in claims:
    for x in range(0, claim['width']):
        for y in range(0, claim['height']):
            if square[claim['dist_from_top'] + y][claim['dist_from_left'] + x] == '.':
                square[claim['dist_from_top'] + y][claim['dist_from_left'] + x] = claim['id']
            else:
                square[claim['dist_from_top'] + y][claim['dist_from_left'] + x] = 'X'

print(sum(x.count('X') for x in square))
for l in square:
    print(l)
