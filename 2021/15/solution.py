from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    cavern_risks = [[int(i) for i in list(line)] for line in problem_input.splitlines()]
    tracker = []
    height, width = len(cavern_risks), len(cavern_risks[0])

    for ypos in range(height):
        tracker.append([])
        for xpos in range(width):
            if ypos == 0 and xpos == 0:
                current_risk = 0
            else:
                current_risk = cavern_risks[ypos][xpos]
            
            risks = [current_risk]
            neighbors = []

            if ypos + 1 < height and ypos + 1 < len(tracker):
                neighbors.append(tracker[ypos + 1][xpos])
            if ypos - 1 >= 0:
                neighbors.append(tracker[ypos - 1][xpos])
            if xpos + 1 < width and xpos + 1 < len(tracker[ypos]):
                neighbors.append(tracker[ypos][xpos + 1])
            if xpos - 1 >= 0:
                neighbors.append(tracker[ypos][xpos - 1])

            if neighbors:
                risks.append(min(neighbors))

            tracker[ypos].append(sum(risks))

    return tracker[-1][-1]


aoc_utils.run(answer, cases)
