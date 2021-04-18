# -*- coding:utf-8 -*-

"""Implementation Dijkstra’s algorithm."""

from graph_algorithms.data_structure.priority_queue.priority_queue import make_priority_queue
from graph_algorithms.data_structure.priority_queue.priority_queue import extract_min
from graph_algorithms.data_structure.priority_queue.priority_queue import set_priority
from graph_algorithms.data_structure.priority_queue.priority_queue import decrease_priority
from graph_algorithms.data_structure.priority_queue.priority_queue import is_empty

from graph_algorithms.data_structure.distance import make_distances
from graph_algorithms.data_structure.distance import set_distance
from graph_algorithms.algorithms.relax import relax
from graph_algorithms.algorithms.relax import edge_weight

from graph_algorithms.exception.graph_exception import NotContainsElementException
from graph_algorithms.exception.messages import not_contains_vertex_message

from graph_algorithms.exception.graph_exception import GraphIsEmptyException
from graph_algorithms.exception.messages import graph_is_empty_message


def dijkstra(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Raises:
        GraphIsEmptyException: if graph is empty
        NotContainsElementException: if graph not contains start vertex

    Returns:
        distances: collection storing the distance from the starting vertex to the rest
    """
    if graph.is_empty:
        raise GraphIsEmptyException(graph_is_empty_message())
    if start_vertex.identifier not in graph:
        raise NotContainsElementException(not_contains_vertex_message(start_vertex.identifier))
    return _dijkstra(graph, start_vertex)


def _dijkstra(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Returns:
        distances: collection storing the distance from the starting vertex to the rest

    """
    distance = make_distances(graph)
    priority_queue = make_priority_queue(graph)

    set_distance(start_vertex, 0, distance)
    set_priority(start_vertex, 0, priority_queue)

    while not is_empty(priority_queue):
        vertex = extract_min(priority_queue)
        for adjacent_vertex in vertex:
            if relax(vertex, adjacent_vertex, distance):
                weight = edge_weight(vertex, adjacent_vertex, distance)
                decrease_priority(adjacent_vertex, weight, priority_queue)
    return distance
