"""Implementation iterative breadth-first search."""

from algorithms.exception.graph_exception import GraphIsEmptyException
from algorithms.exception.messages import graph_is_empty_message

from algorithms.exception.graph_exception import GraphNotContainsVertexException
from algorithms.exception.messages import graph_not_contains_vertex_message

from algorithms.paths_in_graph.bfs.queue import make_queue, enqueue, dequeue, is_empty
from algorithms.paths_in_graph.distance import get_distance, make_distances, not_visited, set_distance


def bfs(graph, start_vertex):
    """Return the distance from the starting vertex to the rest.

    Args:
        graph: graph for search
        start_vertex: start vertex for search

    Raises:
        GraphIsEmptyException: if graph is emoty
        GraphNotContainsVertexException: if graph not contains start vertex

    Returns:
        distances: collection storing the distance from the starting vertex to the rest

    """
    if graph.is_empty:
        raise GraphIsEmptyException(graph_is_empty_message())
    if start_vertex.identifier not in graph:
        raise GraphNotContainsVertexException(graph_not_contains_vertex_message(start_vertex.identifier))
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
