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
    # Set to correct starting position
    dial_tracker = rotate_forward(list(range(0,100)), 50)
  
    # Part one counts if the dial lands at 0 after rotation, part two counts if we ever pass zero while rotating
    count_landing_at_zero = 0
    count_passing_through_zero = 0

    for instruction in problem_input.splitlines():
        direction = instruction[0]
        ticks = int(instruction[1:])
        if direction == "R":
            for i in range(ticks):
                dial_tracker = rotate_forward(dial_tracker, 1)
                if dial_tracker[0] == 0:
                    count_passing_through_zero += 1 
            if dial_tracker[0] == 0:
                count_landing_at_zero += 1
        elif direction == "L":
            for i in range(ticks):
                dial_tracker = rotate_backward(dial_tracker, 1)
                if dial_tracker[0] == 0:
                    count_passing_through_zero += 1 
            if dial_tracker[0] == 0:
                count_landing_at_zero += 1

    if level == 1: 
        return count_landing_at_zero
    
    if level == 2:
        return count_passing_through_zero
        
aoc_utils.run(answer, cases)
