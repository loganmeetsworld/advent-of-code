def build_graph(coords, max_x, max_y):
    graph = [[''] * max_x] * max_y
    for x in range(max_x):
        for y in range(max_y):
            for coord in coords:
                dist = find_shortest_distance(coord, [x, y])
                graph[x].append = {coord: dist}
    return graph


def dimensions(coords):
    max_x = max([c[0] for c in coords])
    max_y = max([c[1] for c in coords])
    return max_x, max_y


def find_shortest_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


print("Part 1:")
coords = [[int(c) for c in cs.split(', ')] for cs in open('input.txt', 'r').read().strip().splitlines()] # noqa
max_x, max_y = dimensions(coords)
graph = build_graph(coords, max_x, max_y)

