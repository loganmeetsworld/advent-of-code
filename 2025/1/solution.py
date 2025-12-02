from aoc_utils import aoc_utils
from tests import cases

def rotate_forward(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

def rotate_backward(arr, k):
    n = len(arr)
    k = k % n
    return arr[n - k:] + arr[:n - k]

def answer(problem_input, level, test=False):
    arr = rotate_forward(list(range(0,100)), 50)
    part_2_count = 0
    part_1_count = 0
    for line in problem_input.splitlines():
        direction = line[0]
        ticks = int(line[1:])
        if direction == "R":
            for i in range(ticks):
                arr = rotate_forward(arr, 1)
                if arr[0] == 0:
                    part_2_count += 1 
            if arr[0] == 0:
                part_1_count += 1
        elif direction == "L":
            for i in range(ticks):
                arr = rotate_backward(arr, 1)
                if arr[0] == 0:
                    part_2_count += 1 
            if arr[0] == 0:
                part_1_count += 1

    if level == 1: 
        return part_1_count
    
    if level == 2:
        return part_2_count
        
aoc_utils.run(answer, cases)
