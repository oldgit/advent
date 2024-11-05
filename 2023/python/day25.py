import random
import sys
from collections import defaultdict

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]


class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = set()

    def add_edge(self, u, v):
        self.edges.append([u, v])
        self.vertices.add(u)
        self.vertices.add(v)


def get_graph():
    graph = Graph()
    with open(f"data/{DAY}/input.txt") as fin:
        lines = fin.read().strip().split("\n")
        for LINE in lines:
            k, vt = LINE.split(": ")
            vs = vt.split(" ")
            for vi in vs:
                graph.add_edge(k, vi)
    return graph


def find_parent(parent: dict[str, str], name: str):
    if parent[name] == name:
        return name
    return find_parent(parent, parent[name])


def union(parent: dict[str, str], rank: dict[str, int], x: str, y: str):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def get_partitions(parent: dict[str, str], vertices: set[str]):
    # Group vertices by their parent to get partitions
    partitions = defaultdict(set)
    for vertex in vertices:
        root = find_parent(parent, vertex)
        partitions[root].add(vertex)
    return list(partitions.values())


def karger_min_cut(graph: Graph):
    vertices = len(graph.vertices)
    parent = {}
    rank = {}

    # Initialize parent and rank arrays
    for vertex in graph.vertices:
        parent[vertex] = vertex
        rank[vertex] = 0

    # Contract edges until only 2 vertices remain
    vertices_left = vertices
    while vertices_left > 2:
        # Pick a random edge
        edge_index = random.randint(0, len(graph.edges) - 1)
        edge = graph.edges[edge_index]

        # Find the sets of vertices
        set1 = find_parent(parent, edge[0])
        set2 = find_parent(parent, edge[1])

        # If vertices belong to different sets, contract them
        if set1 != set2:
            vertices_left -= 1
            union(parent, rank, set1, set2)

    # Count crossing edges (cut edges)
    cut_edges = 0
    for edge in graph.edges:
        set1 = find_parent(parent, edge[0])
        set2 = find_parent(parent, edge[1])
        if set1 != set2:
            cut_edges += 1

    # Get the two partitions
    partitions = get_partitions(parent, graph.vertices)
    return cut_edges, partitions


def repeated_karger(graph, expected_min_cut):
    cut_value = 100
    partitions = None

    while cut_value > expected_min_cut:
        cut_value, partitions = karger_min_cut(graph)

    return cut_value, partitions


def part_1():
    expected_min_cut = 3
    min_cut, partitions = repeated_karger(get_graph(), expected_min_cut)
    assert min_cut == expected_min_cut
    result = len(partitions[0]) * len(partitions[1])
    return result


p1_result = part_1()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
print(f"{DAY} Part 1: {p1_result}")
