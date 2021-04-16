# -*- coding:utf-8 -*-

import pytest

from graph_algorithms.algorithms.bfs.bfs import bfs
from graph_algorithms.data_structure.graph.graph import Graph
from graph_algorithms.data_structure.graph.graph import Vertex

from graph_algorithms.exception.graph_exception import NotContainsVertexException
from graph_algorithms.exception.messages import not_contains_vertex_message

from graph_algorithms.exception.graph_exception import GraphIsEmptyException
from graph_algorithms.exception.messages import graph_is_empty_message


def test_bfs_positive1():
    graph = Graph()

    graph.create_vertex_by_id('A')

    distance = bfs(graph, graph.get_vertex_by_id('A'))

    assert distance['A'] == 0

def test_bfs_positive2():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')

    distance = bfs(graph, graph.get_vertex_by_id('A'))

    assert distance['A'] == 0
    assert distance['B'] == 1
    assert distance['C'] == 1

    assert distance['D'] is None


def test_bfs_positive3():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')
    graph.create_vertex_by_id('E')
    graph.create_vertex_by_id('S')

    graph.add_edge('E', 'S')
    graph.add_edge('E', 'D')

    graph.add_edge('S', 'E')
    graph.add_edge('S', 'D')
    graph.add_edge('S', 'C')
    graph.add_edge('S', 'A')

    graph.add_edge('C', 'S')
    graph.add_edge('C', 'B')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'S')

    graph.add_edge('B', 'A')
    graph.add_edge('B', 'C')

    distance = bfs(graph, graph.get_vertex_by_id('S'))

    assert distance['S'] == 0

    assert distance['A'] == 1
    assert distance['C'] == 1
    assert distance['D'] == 1
    assert distance['E'] == 1

    assert distance['B'] == 2


def test_bfs_negative1():
    graph = Graph()

    with pytest.raises(GraphIsEmptyException) as exception_info:
        bfs(graph, Vertex('S'))

    assert str(exception_info.value) == graph_is_empty_message()


def test_bfs_negative2():
    graph = Graph()

    graph.create_vertex_by_id('A')

    with pytest.raises(NotContainsVertexException) as exception_info:
        bfs(graph, Vertex('S'))

    assert str(exception_info.value) == not_contains_vertex_message('S')
