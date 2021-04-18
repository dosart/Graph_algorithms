# -*- coding:utf-8 -*-

"""Edge data structure tests."""

from graph_algorithms.data_structure.graph.graph import Graph


def test_edges():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')

    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'C', 20)
    graph.add_edge('B', 'C', 20)

    edges = graph.edges

    assert len(edges) == 3

    first = edges[0]
    assert first.first.identifier == 'A'
    assert first.second.identifier == 'B'
    assert first.weight == 10

    second = edges[1]
    assert second.first.identifier == 'A'
    assert second.second.identifier == 'C'
    assert second.weight == 20

    third = edges[2]
    assert third.first.identifier == 'B'
    assert third.second.identifier == 'C'
    assert third.weight == 20