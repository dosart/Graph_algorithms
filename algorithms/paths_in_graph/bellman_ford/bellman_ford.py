"""Implementation Bellman-Ford’s algorithm."""

from algorithms.paths_in_graph.relax import relax

from algorithms.paths_in_graph.distance import make_distances
from algorithms.paths_in_graph.distance import set_distance

from algorithms.exception.graph_exception import NotContainsVertexException
from algorithms.exception.messages import not_contains_vertex_message

from algorithms.exception.graph_exception import GraphIsEmptyException
from algorithms.exception.messages import graph_is_empty_message


def bellman_ford(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Raises:
        GraphIsEmptyException: if graph is empty
        NotContainsVertexException: if graph not contains start vertex

    Returns:
        distances: collection storing the distance from the starting vertex to the rest
    """
    if graph.is_empty:
        raise GraphIsEmptyException(graph_is_empty_message())
    if start_vertex.identifier not in graph:
        raise NotContainsVertexException(not_contains_vertex_message(start_vertex.identifier))
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
