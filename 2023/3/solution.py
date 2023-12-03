from aoc_utils import aoc_utils
from tests import cases

def is_part_adjacent(rows, y_idx, x_idx):
    height = len(rows)
    width = len(rows[0])
    if 0 < y_idx < height and 0 < x_idx - 1 < width:
        if rows[y_idx][x_idx - 1] != '.' and not rows[y_idx][x_idx - 1].isnumeric():
            return True 

    if 0 < y_idx < height and 0 < x_idx + 1 < width:
        if rows[y_idx][x_idx + 1] != '.' and not rows[y_idx][x_idx + 1].isnumeric():
            return True 

    if 0 < y_idx - 1 < height and 0 < x_idx < width:
        if rows[y_idx - 1][x_idx] != '.' and not rows[y_idx - 1][x_idx]. isnumeric():
            return True 

    if 0 < y_idx + 1 < height and 0 < x_idx < width:
        if rows[y_idx + 1][x_idx] != '.' and not rows[y_idx + 1][x_idx].isnumeric():
            return True 

    if 0 < y_idx - 1 < height and 0 < x_idx + 1 < width:
        if rows[y_idx - 1][x_idx + 1] != '.' and not rows[y_idx - 1][x_idx + 1].isnumeric():
            return True 

    if 0 < y_idx - 1 < height and 0 < x_idx - 1 < width:
        if rows[y_idx - 1][x_idx - 1] != '.' and not rows[y_idx - 1][x_idx - 1].isnumeric():
            return True 

    if 0 < y_idx + 1 < height and 0 < x_idx + 1 < width:
        if rows[y_idx + 1][x_idx + 1] != '.' and not rows[y_idx + 1][x_idx + 1].isnumeric():
            return True 

    if 0 < y_idx + 1 < height and 0 < x_idx - 1 < width:
        if rows[y_idx + 1][x_idx - 1] != '.' and not rows[y_idx + 1][x_idx - 1].isnumeric():
            return True 


def answer(problem_input, level, test=False):
    rows = problem_input.splitlines()
    col_length = len(rows[0])
    parts_sum = 0

    y_idx = 0
    for row in rows:
        x_idx = 0
        while col_length > x_idx:
            part_adjacent = False
            if not row[x_idx].isnumeric():
                x_idx += 1
                continue

            if is_part_adjacent(rows, y_idx, x_idx):
                part_adjacent = True

            next_idx = x_idx + 1
            number = [row[x_idx]]
            while next_idx < col_length  and row[next_idx].isnumeric():
                number.append(row[next_idx])
                if is_part_adjacent(rows, y_idx, next_idx):
                    part_adjacent = True
                next_idx += 1
                x_idx += 1
        
            print(number)
            if part_adjacent:
                parts_sum += int(''.join(number))
            
            x_idx += 1
        
        y_idx += 1

    return parts_sum

aoc_utils.run(answer, cases)
