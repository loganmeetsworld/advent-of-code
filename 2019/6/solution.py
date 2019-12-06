import networkx as nx

from aoc_utils import aoc_utils
from tests import cases


def orbit_count(edges):
    graph = nx.Graph()
    [graph.add_edge(edge[0], edge[1]) for edge in edges]
    total = 0
    for node in graph.nodes:
        total += len(nx.descendants(graph, node))
    return total


def shortest_path(edges):
    graph = nx.Graph()
    [graph.add_edge(edge[0], edge[1]) for edge in edges]
    return nx.shortest_path_length(graph, 'YOU', 'SAN') - 2


def answer(problem_input, level, test=False):
    edges = [e.split(')') for e in problem_input.splitlines()]
    return orbit_count(edges) if level == 1 else shortest_path(edges)


aoc_utils.run(answer, cases)
