# -*- coding:utf-8 -*-

"""Implementation iterative breadth-first search."""

from graph_algorithms.exception.graph_exception import DataStructureIsEmptyException
from graph_algorithms.exception.messages import data_structure_is_empty_message

from graph_algorithms.exception.graph_exception import NotContainsElementException
from graph_algorithms.exception.messages import not_contains_vertex_message

from graph_algorithms.algorithms.bfs.queue import make_queue, enqueue, dequeue, is_empty
from graph_algorithms.data_structure.distance import get_distance, make_distances, not_visited, set_distance


def bfs(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Raises:
        DataStructureIsEmptyException: if graph is emoty
        NotContainsElementException: if graph not contains start vertex

    Returns:
        distances: collection storing the distance from the starting vertex to the rest

    """
    if graph.is_empty:
        raise DataStructureIsEmptyException(data_structure_is_empty_message())
    if start_vertex.identifier not in graph:
        raise NotContainsElementException(not_contains_vertex_message(start_vertex.identifier))
    return _bfs(graph, start_vertex)


def _bfs(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Returns:
        distances: collection storing the distance from the starting vertex to the rest

    """
    distances = make_distances(graph)
    set_distance(start_vertex, 0, distances)

    vertices = make_queue()
    enqueue(vertices, start_vertex)

    while not is_empty(vertices):
        vertex = dequeue(vertices)
        for adjacent_vertex in vertex:
            if not_visited(adjacent_vertex, distances):
                enqueue(vertices, adjacent_vertex)
                distance = get_distance(vertex, distances)
                set_distance(adjacent_vertex, distance + 1, distances)
    return distances
