"""Implementation Bellman-Ford’s algorithm."""

from graph_algorithms.algorithms.relax import relax

from graph_algorithms.data_structure.distance import make_distances
from graph_algorithms.data_structure.distance import set_distance

from graph_algorithms.exception.graph_exception import NotContainsElementException
from graph_algorithms.exception.messages import not_contains_vertex_message

from graph_algorithms.exception.graph_exception import DataStructureIsEmptyException
from graph_algorithms.exception.messages import data_structure_is_empty_message


def bellman_ford(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Raises:
        DataStructureIsEmptyException: if graph is empty
        NotContainsElementException: if graph not contains start vertex

    Returns:
        distances: collection storing the distance from the starting vertex to the rest
    """
    if graph.is_empty:
        raise DataStructureIsEmptyException(data_structure_is_empty_message())
    if start_vertex.identifier not in graph:
        raise NotContainsElementException(not_contains_vertex_message(start_vertex.identifier))
    return _bellman_ford(graph, start_vertex)


def _bellman_ford(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Returns:
        distances: collection storing the distance from the starting vertex to the rest
    """
    distance = make_distances(graph)
    set_distance(start_vertex, 0, distance)

    for _ in range(len(graph)):
        for edge in graph.edges:
            relax(edge.first, edge.second, distance)
    return distance
