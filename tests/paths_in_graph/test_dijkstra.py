# -*- coding:utf-8 -*-

import pytest

from graph_algorithms.data_structure.graph.graph import Graph
from graph_algorithms.data_structure.graph.vertex import Vertex

from graph_algorithms.algorithms.dijkstra.dijkstra import dijkstra
from graph_algorithms.algorithms.bellman_ford.bellman_ford import bellman_ford

from graph_algorithms.data_structure.distance import get_distance

from graph_algorithms.exception.graph_exception import NotContainsVertexException
from graph_algorithms.exception.messages import not_contains_vertex_message

from graph_algorithms.exception.graph_exception import GraphIsEmptyException
from graph_algorithms.exception.messages import graph_is_empty_message


@pytest.mark.parametrize("f", [dijkstra, bellman_ford])
def test_positive1(f):
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')
    graph.create_vertex_by_id('E')

    graph.add_edge('A', 'C', 2)
    graph.add_edge('A', 'B', 4)

    graph.add_edge('B', 'C', 3)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('B', 'E', 3)

    graph.add_edge('C', 'B', 1)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('C', 'E', 5)

    graph.add_edge('E', 'D', 1)

    distance = f(graph, graph.get_vertex_by_id('A'))

    distance_to_c = get_distance(graph.get_vertex_by_id('C'), distance)
    assert distance_to_c == 2

    distance_to_b = get_distance(graph.get_vertex_by_id('B'), distance)
    assert distance_to_b == 3

    distance_to_e = get_distance(graph.get_vertex_by_id('E'), distance)
    assert distance_to_e == 6

    distance_to_d = get_distance(graph.get_vertex_by_id('D'), distance)
    assert distance_to_d == 5

@pytest.mark.parametrize("f", [dijkstra, bellman_ford])
def test_dijkstra_positive2(f):
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')

    graph.add_edge('A', 'C', 2)
    graph.add_edge('A', 'B', 4)

    distance = f(graph, graph.get_vertex_by_id('A'))

    distance_to_b = get_distance(graph.get_vertex_by_id('B'), distance)
    assert distance_to_b == 4

    distance_to_c = get_distance(graph.get_vertex_by_id('C'), distance)
    assert distance_to_c == 2

    distance_to_d = get_distance(graph.get_vertex_by_id('D'), distance)
    assert distance_to_d is None


@pytest.mark.parametrize("f", [dijkstra, bellman_ford])
def test_dijkstra_negative1(f):
    graph = Graph()

    with pytest.raises(GraphIsEmptyException) as exception_info:
        f(graph, Vertex('A'))

    assert str(exception_info.value) == graph_is_empty_message()

@pytest.mark.parametrize("f", [dijkstra, bellman_ford])
def test_dijkstra_negative2(f):
    graph = Graph()

    graph.create_vertex_by_id('A')

    with pytest.raises(NotContainsVertexException) as exception_info:
        f(graph, Vertex('B'))

    assert str(exception_info.value) == not_contains_vertex_message('B')
