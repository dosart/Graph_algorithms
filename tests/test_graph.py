# -*- coding:utf-8 -*-

"""Tests of graphs."""

import pytest

from graph_algorithms.data_structure.graph.graph import Graph
from graph_algorithms.data_structure.graph.vertex import Vertex

from graph_algorithms.exception.graph_exception import GraphContainsVertexExemption
from graph_algorithms.exception.graph_exception import GraphIsEmptyException
from graph_algorithms.exception.graph_exception import NotContainsElementException

from graph_algorithms.exception.messages import graph_contains_vertex_message
from graph_algorithms.exception.messages import graph_is_empty_message
from graph_algorithms.exception.messages import not_contains_vertex_message


def test_make_graph():
    graph = Graph()

    assert graph.size == 0
    assert graph.is_empty == True
    assert len(graph) == 0


def test_add_vertices():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')

    assert graph.size == 3
    assert len(graph) == 3
    assert graph.is_empty == False


def test_add_vertex_second_time():
    graph = Graph()

    graph.create_vertex_by_id('A')

    with pytest.raises(GraphContainsVertexExemption) as exception_info:
        graph.create_vertex_by_id('A')
    assert str(exception_info.value) == graph_contains_vertex_message('A')


def test_add_edge_in_empty_graph():
    graph = Graph()

    with pytest.raises(GraphIsEmptyException) as exception_info:
        graph.add_edge('A', 'B')
    assert str(exception_info.value) == graph_is_empty_message()


def test_vertex_not_found1():
    graph = Graph()
    graph.create_vertex_by_id('A')

    with pytest.raises(NotContainsElementException) as exception_info:
        graph.add_edge('A', 'B')
    assert str(exception_info.value) == not_contains_vertex_message('B')


def test_vertex_not_found2():
    graph = Graph()
    graph.create_vertex_by_id('B')

    with pytest.raises(NotContainsElementException) as exception_info:
        graph.add_edge('A', 'B')
    assert str(exception_info.value) == not_contains_vertex_message('A')


def test_get_graph_iterator():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')

    for vertex in graph:
        pass


def test_contains_positive():
    graph = Graph()

    graph.create_vertex_by_id('K')
    graph.create_vertex_by_id('L')
    graph.create_vertex_by_id('M')

    assert True is ('L' in graph)


def test_contains_negative():
    graph = Graph()

    graph.create_vertex_by_id('K')
    graph.create_vertex_by_id('L')
    graph.create_vertex_by_id('M')

    assert False is ('F' in graph)


def test_get_vertex_by_id_positive():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    length = len(graph)

    vertex = graph.get_vertex_by_id('A')

    assert vertex.identifier == 'A'
    assert length == len(graph)


def test_get_vertex_by_id_negative1():
    graph = Graph()

    graph.create_vertex_by_id('B')

    with pytest.raises(NotContainsElementException) as exception_info:
        vertex = graph.get_vertex_by_id('A')

    assert str(exception_info.value) == not_contains_vertex_message('A')


def test_get_vertex_by_id_negative2():
    graph = Graph()

    with pytest.raises(GraphIsEmptyException) as exception_info:
        vertex = graph.get_vertex_by_id('A')

    assert str(exception_info.value) == graph_is_empty_message()


def test_edge_weight_to_nagative():
    vertex_s = Vertex('S')
    vertex_a = Vertex('A')
    vertex_b = Vertex('B')

    vertex_s.add_adjacent_vertex(vertex_a)

    with pytest.raises(NotContainsElementException) as exception_info:
        weight = vertex_s.edge_weight_to(vertex_b)

    assert str(exception_info.value) == not_contains_vertex_message('B')


def test_edge_weight_to_positive():
    vertex_s = Vertex('S')
    vertex_a = Vertex('A')

    vertex_s.add_adjacent_vertex(vertex_a, 5)

    weight = vertex_s.edge_weight_to(vertex_a)

    assert weight == 5


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
