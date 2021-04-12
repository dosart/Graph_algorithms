# -*- coding:utf-8 -*-

"""Implementation Dijkstra’s algorithm."""

from algorithms.paths_in_graph.priority_queue.priority_queue import make_priority_queue
from algorithms.paths_in_graph.priority_queue.priority_queue import extract_min
from algorithms.paths_in_graph.priority_queue.priority_queue import set_priority
from algorithms.paths_in_graph.priority_queue.priority_queue import decrease_priority
from algorithms.paths_in_graph.priority_queue.priority_queue import is_empty

from algorithms.paths_in_graph.distance import make_distances
from algorithms.paths_in_graph.distance import get_distance
from algorithms.paths_in_graph.distance import set_distance
from algorithms.paths_in_graph.distance import to_int

from algorithms.exception.graph_exception import NotContainsVertexException
from algorithms.exception.messages import not_contains_vertex_message

from algorithms.exception.graph_exception import GraphIsEmptyException
from algorithms.exception.messages import graph_is_empty_message


def dijkstra(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Raises:
        GraphIsEmptyException: if graph is emoty
        NotContainsVertexException: if graph not contains start vertex

    Returns:
        distances: collection storing the distance from the starting vertex to the rest
    """
    if graph.is_empty:
        raise GraphIsEmptyException(graph_is_empty_message())
    if start_vertex.identifier not in graph:
        raise NotContainsVertexException(not_contains_vertex_message(start_vertex.identifier))
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
            weight = _edge_weight(vertex, adjacent_vertex, distance)
            if _get_distance(adjacent_vertex, distance) > weight:
                set_distance(adjacent_vertex, weight, distance)
                decrease_priority(adjacent_vertex, weight, priority_queue)
    return distance


def _edge_weight(vertex, adjacent_vertex, distance):
    return to_int(get_distance(vertex, distance)) + vertex.edge_weight_to(adjacent_vertex)


def _get_distance(vertex, distance):
    return to_int(get_distance(vertex, distance))
