from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    tree_map = [list(col) for col in problem_input.splitlines()]
    visible_count = 0
    scenic_scores = []
    for row_idx, row in enumerate(tree_map):
        for tree_idx, tree in enumerate(row):
            # If our tree is on the edge, it is visible, move on
            if tree_idx == 0 or row_idx == 0 or tree_idx + 1 == len(row) or len(tree_map) == row_idx + 1:
                visible_count += 1
                continue

            ups_counter = 1
            ups_visible = 0
            ups = []
            view_blocked_up = False
            while row_idx - ups_counter >= 0:
                up = int(tree_map[row_idx - ups_counter][tree_idx])
                if not view_blocked_up:
                    ups_visible += 1

                if up >= int(tree):
                    view_blocked_up = True
                ups.append(up)
                ups_counter += 1

            downs_counter = 1
            downs_visible = 0
            downs = []
            view_blocked_down = False
            while row_idx + downs_counter < len(tree_map):
                down = int(tree_map[row_idx + downs_counter][tree_idx])
                if not view_blocked_down:
                    downs_visible += 1

                if down >= int(tree):
                    view_blocked_down = True

                downs.append(down)
                downs_counter += 1

            rights_counter = 1
            rights_visible = 0
            rights = []
            view_blocked_right = False
            while tree_idx + rights_counter < len(row):
                right = int(tree_map[row_idx][tree_idx + rights_counter])
                if not view_blocked_right:
                    rights_visible += 1

                if right >= int(tree):
                    view_blocked_right = True

                rights.append(right)
                rights_counter += 1

            lefts_counter = 1
            lefts_visible = 0
            lefts = []
            view_blocked_left = False
            while tree_idx - lefts_counter >= 0:
                left = int(tree_map[row_idx][tree_idx - lefts_counter])
                if not view_blocked_left:
                    lefts_visible += 1

                if left >= int(tree):
                    view_blocked_left = True

                lefts.append(left)
                lefts_counter += 1

            scenic_score = downs_visible * ups_visible * rights_visible * lefts_visible
            scenic_scores.append(scenic_score)

            if int(tree) > max(ups) or int(tree) > max(downs) or int(tree) > max(lefts) or int(tree) > max(rights):
                visible_count += 1

    if level == 1:
        return visible_count
    else:
        return max(scenic_scores)


aoc_utils.run(answer, cases)
