# -*- coding:utf-8 -*-

"""Tests of Kruskal's algorithm."""

from graph_algorithms.algorithms.kruskal.kruskal import kruskal
from graph_algorithms.data_structure.graph.graph import Graph


def test_kruskal1():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')
    graph.create_vertex_by_id('E')
    graph.create_vertex_by_id('F')

    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 1)

    graph.add_edge('B', 'A', 2)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 1)

    graph.add_edge('D', 'C', 2)
    graph.add_edge('D', 'E', 3)
    graph.add_edge('D', 'F', 4)

    graph.add_edge('C', 'D', 2)
    graph.add_edge('C', 'E', 3)
    graph.add_edge('C', 'A', 1)
    graph.add_edge('C', 'B', 2)

    graph.add_edge('E', 'D', 3)
    graph.add_edge('E', 'C', 3)
    graph.add_edge('E', 'F', 2)

    graph.add_edge('F', 'E', 2)
    graph.add_edge('F', 'D', 4)

    edges = kruskal(graph)

    assert len(edges) == 5
    assert find_edge('A', 'B', edges) is not None
    assert find_edge('A', 'C', edges) is not None
    assert find_edge('B', 'D', edges) is not None
    assert find_edge('D', 'E', edges) is not None
    assert find_edge('E', 'F', edges) is not None


def test_kruskal2():
    graph = Graph()

    edges = kruskal(graph)

    assert len(edges) == 0


def test_kruskal3():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')

    graph.add_edge('A', 'C', 5)
    graph.add_edge('B', 'C', 2)

    graph.add_edge('C', 'A', 5)
    graph.add_edge('C', 'B', 2)

    edges = kruskal(graph)

    assert len(edges) == 2
    assert find_edge('A', 'C', edges)
    assert find_edge('B', 'C', edges)


def find_edge(first_id, second_id, edges):
    res_one = next((edge for edge in edges if edge.first.identifier == first_id and edge.second.identifier == second_id), None)
    res_two = next((edge for edge in edges if edge.first.identifier == second_id and edge.second.identifier == first_id), None)

    return res_one or res_two
