import re
instructions = [[int(r) for r in re.findall(r'-?\d+', i)] for i in open('input.txt').readlines()] # noqa

for t in range(100000):
    min_x = min([x for x, y, _, _ in instructions])
    max_x = max([x for x, y, _, _ in instructions])
    min_y = min([y for x, y, _, _ in instructions])
    max_y = max([y for x, y, _, _ in instructions])

    # guess at the width to get in the right bounds
    width = 150
    if min_x + width >= max_x and min_y + width >= max_y:
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                if (x, y) in [(px, py) for px, py, _, _ in instructions]:
                    print('#'),
                else:
                    print('.'),
            print("\n")

    # add velocity
    for i in instructions:
        i[0] += i[2]
        i[1] += i[3]
