from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    tree_map = [list(col) for col in problem_input.splitlines()]
    visible_count = 0
    scenic_scores = []
    for rowi, row in enumerate(tree_map):
        for coli, col in enumerate(row):
            ups_counter = 1
            ups_visible = 0
            heighest_up_seen = 9
            ups = []
            while rowi - ups_counter >= 0:
                if int(tree_map[rowi - ups_counter][coli]) <= heighest_up_seen:
                    ups_visible += 1
                    heighest_up_seen = int(tree_map[rowi - ups_counter][coli])
                ups.append(tree_map[rowi - ups_counter][coli])
                ups_counter += 1

            downs_counter = 1
            downs_visible = 0
            heighest_down_seen = 9
            downs = []
            while rowi + downs_counter < len(tree_map):
                if int(tree_map[rowi + downs_counter][coli]) <= heighest_down_seen:
                    downs_visible += 1
                    heighest_down_seen = int(tree_map[rowi + downs_counter][coli])

                downs.append(tree_map[rowi + downs_counter][coli])
                downs_counter += 1

            rights_counter = 1
            rights_visible = 0
            heighest_right_seen = 9
            rights = []
            while coli + rights_counter < len(row):
                if int(tree_map[rowi][coli + rights_counter]) <= heighest_right_seen:
                    rights_visible += 1
                    heighest_right_seen = int(tree_map[rowi][coli + rights_counter])

                rights.append(tree_map[rowi][coli + rights_counter])
                rights_counter += 1

            lefts_counter = 1
            lefts_visible = 0
            heighest_left_seen = 9
            lefts = []
            while coli - lefts_counter >= 0:
                if int(tree_map[rowi][coli - lefts_counter]) <= heighest_left_seen:
                    lefts_visible += 1
                    heighest_left_seen = int(tree_map[rowi][coli - lefts_counter])

                lefts.append(tree_map[rowi][coli - lefts_counter])
                lefts_counter += 1

            scenic_score = downs_visible * ups_visible * rights_visible * lefts_visible
            if scenic_score == 91800:
                print(rowi)
                print(coli)
            scenic_scores.append(scenic_score)

            if coli == 0 or rowi == 0 or coli + 1 == len(row) or len(tree_map) == rowi + 1:
                visible_count += 1
                continue

            if col > max(ups) or col > max(downs) or col > max(lefts) or col > max(rights):
                visible_count += 1

    if level == 1:
        return visible_count
    else:
        return max(scenic_scores)


aoc_utils.run(answer, cases)
