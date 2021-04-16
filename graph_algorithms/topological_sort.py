# -*- coding:utf-8 -*-

"""Implementation topological sort don't using algorithm DFS."""

from collections import deque

from graph_algorithms.dfs.contains_circle import contains_circle
from graph_algorithms.exception.graph_exception import GraphContainsCircleException
from graph_algorithms.exception.messages import sorting_not_possible_message


def topological_sort(graph):
    """Return vertices in sorted_array.

    Args:
        graph: graph for sort

    Raises:
        GraphContainsCircleException: if graph contains circle

    Returns:
        sorted_array (list): vertices in sorted_array
    """
    if contains_circle(graph):
        raise GraphContainsCircleException(sorting_not_possible_message())

    sorted_array = []

    degrees = _count_degrees(graph)
    sources = _get_sources(degrees)
    while sources:
        source = _get_source(sources)
        sorted_array.append(source)

        for adjacent_vertex in source:
            degrees[adjacent_vertex] -= 1
            if degrees[adjacent_vertex] == 0:
                sources.append(adjacent_vertex)

    return sorted_array


def _count_degrees(graph):
    in_degree = {vertex: 0 for vertex in graph}
    for vertex in graph:
        for adjacent_vertex in vertex:
            in_degree[adjacent_vertex] += 1
    return in_degree


def _get_sources(degrees):
    return deque([vertex for vertex, degree in degrees.items() if degree == 0])


def _get_source(sources):
    return sources.popleft()
