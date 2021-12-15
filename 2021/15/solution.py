import networkx as nx

from aoc_utils import aoc_utils
from tests import cases


def create_graph(cavern_risks, height, width):
    graph = nx.grid_2d_graph(height, width, create_using=nx.DiGraph)
    for x in range(width):
        for y in range(height):
            neighbors = [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1)
            ]
            for neighbour in neighbors:
                if 0 <= x <= width and 0 <= y <= height:
                    graph.add_edge(neighbour, (x, y), weight=cavern_risks[x][y])
    return graph


def answer(problem_input, level, test=False):
    cavern_risks = [[int(i) for i in list(line)] for line in problem_input.splitlines()]
    height, width = len(cavern_risks), len(cavern_risks[0])
    graph = create_graph(cavern_risks, height, width)
    return nx.shortest_path_length(
        graph,
        source=(0, 0),
        target=(height - 1, width - 1),
        weight='weight',
        method='dijkstra'
    )


aoc_utils.run(answer, cases)
