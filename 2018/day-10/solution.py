import re
instructions = [[int(r) for r in re.findall(r'-?\d+', i)] for i in open('input.txt').readlines()] # noqa
seconds_passed = 0
big_number = 100000
possible_width = 150

for t in range(big_number):
    min_x = min([x for x, y, _, _ in instructions])
    max_x = max([x for x, y, _, _ in instructions])
    min_y = min([y for x, y, _, _ in instructions])
    max_y = max([y for x, y, _, _ in instructions])

    # guess at the width to get in the right bounds
    # only print out if we are in the right bounds
    if min_x + possible_width >= max_x and min_y + possible_width >= max_y:
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                if (x, y) in [(px, py) for px, py, _, _ in instructions]:
                    print('#'),
                else:
                    print('.'),
            print("\n")
        print("seconds passed: {}".format(seconds_passed))

    # add velocity
    for i in instructions:
        i[0] += i[2]
        i[1] += i[3]

    seconds_passed += 1
