from aoc_utils import aoc_utils
from tests import cases


def find_asteroids(asteroid_map):
    views = []
    for idx_y, y in enumerate(asteroid_map.splitlines()):
        for idx_x, x in enumerate(list(y)):
            views.append({'text': x, 'x': idx_x, 'y': idx_y})
    asteroids = [v for v in views if v['text'] == '#']
    return asteroids


def sight_line(x_asteroid, y_asteroid, x, y):
    if x_asteroid == x:
        force = '+' if y_asteroid < y else '-'
    else:
        force = '+' if x_asteroid < x else '-'
    try:
        slope = (y_asteroid - y) / (x_asteroid - x)
        return str(slope) + force
    except ZeroDivisionError:
        return f"inf-{force}"


def find_max_viewed(asteroid_map):
    asteroids = find_asteroids(asteroid_map)
    targets = []

    for a in asteroids:
        asteroid_set = set()
        for b in asteroids:
            asteroid_set.add(sight_line(a['x'], a['y'], b['x'], b['y']))
        targets.append(len(asteroid_set))

    return max(targets)


def answer(problem_input, level, test=False):
    max_viewed = find_max_viewed(problem_input)
    return max_viewed


aoc_utils.run(answer, cases)
