"""Tests of graphs."""

import pytest

from algoritms.graph import Graph
from algoritms.exception.graph_exception import GraphContainsVertexExemption
from algoritms.exception.graph_exception import GraphIsEmptyException
from algoritms.exception.graph_exception import GraphNotContainsVertexException


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
    assert str(exception_info.value) == 'A contains in graph'


def test_add_edge_in_empty_graph():
    graph = Graph()

    with pytest.raises(GraphIsEmptyException) as exception_info:
        graph.add_edge('A', 'B')
    assert str(exception_info.value) == 'Graph is empty'


def test_vertex_not_found1():
    graph = Graph()
    graph.create_vertex_by_id('A')

    with pytest.raises(GraphNotContainsVertexException) as exception_info:
        graph.add_edge('A', 'B')
    assert str(exception_info.value) == 'B not found'


def test_vertex_not_found2():
    graph = Graph()
    graph.create_vertex_by_id('B')

    with pytest.raises(GraphNotContainsVertexException) as exception_info:
        graph.add_edge('A', 'B')
    assert str(exception_info.value) == 'A not found'


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

    assert ('L' in graph) == True


def test_contains_negative():
    graph = Graph()

    graph.create_vertex_by_id('K')
    graph.create_vertex_by_id('L')
    graph.create_vertex_by_id('M')

    assert ('F' in graph) == False
