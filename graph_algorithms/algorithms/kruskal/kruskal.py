# -*- coding:utf-8 -*-

"""Implementation Kruskal's algorithm."""

from graph_algorithms.data_structure.disjointed_set_union.disjointed_set_union import DSU


def kruskal(graph):
    """Return minimum spanning tree.

    Args:
        graph: graph data structure

    Returns:
        spanning_tree (set): edges of graph
    """
    suit = _make_set(graph)

    spanning_tree = set()
    edges = graph.get_sorted_edges_by(lambda element: element.weight)
    for edge in edges:
        if not _contains(edge, suit):
            spanning_tree.add(edge)
            suit.unite(edge.first, edge.second)
    return spanning_tree


def _make_set(graph):
    dsu = DSU()
    for vertex in graph:
        dsu.make_set(vertex)
    return dsu


def _contains(edge, dsu):
    return dsu.find(edge.first) == dsu.find(edge.second)
