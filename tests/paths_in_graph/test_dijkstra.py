# -*- coding:utf-8 -*-

import pytest

from algorithms.graph.graph import Graph
from algorithms.graph.vertex import Vertex

from algorithms.paths_in_graph.dijkstra.dijkstra import dijkstra

from algorithms.paths_in_graph.distance import get_distance

from algorithms.exception.graph_exception import NotContainsVertexException
from algorithms.exception.messages import not_contains_vertex_message

from algorithms.exception.graph_exception import GraphIsEmptyException
from algorithms.exception.messages import graph_is_empty_message


def test_dijkstra_positive1():
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

    distance = dijkstra(graph, graph.get_vertex_by_id('A'))

    distance_to_C = get_distance(graph.get_vertex_by_id('C'), distance)
    assert distance_to_C == 2

    distance_to_B = get_distance(graph.get_vertex_by_id('B'), distance)
    assert distance_to_B == 3

    distance_to_E = get_distance(graph.get_vertex_by_id('E'), distance)
    assert distance_to_E == 6

    distance_to_D = get_distance(graph.get_vertex_by_id('D'), distance)
    assert distance_to_D == 5


def test_dijkstra_positive2():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')

    graph.add_edge('A', 'C', 2)
    graph.add_edge('A', 'B', 4)

    distance = dijkstra(graph, graph.get_vertex_by_id('A'))

    distance_to_B = get_distance(graph.get_vertex_by_id('B'), distance)
    assert distance_to_B == 4

    distance_to_C = get_distance(graph.get_vertex_by_id('C'), distance)
    assert distance_to_C == 2

    distance_to_D = get_distance(graph.get_vertex_by_id('D'), distance)
    assert distance_to_D is None


def test_dijkstra_negative1():
    graph = Graph()

    with pytest.raises(GraphIsEmptyException) as exception_info:
        dijkstra(graph, Vertex('A'))

    assert str(exception_info.value) == graph_is_empty_message()


def test_dijkstra_negative2():
    graph = Graph()

    graph.create_vertex_by_id('A')

    with pytest.raises(NotContainsVertexException) as exception_info:
        dijkstra(graph, Vertex('B'))

    assert str(exception_info.value) == not_contains_vertex_message('B')
