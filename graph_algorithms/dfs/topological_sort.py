# -*- coding:utf-8 -*-

"""Implementation topological sort using recursive algorithm DFS."""


from graph_algorithms.dfs.dfs_recursion import dfs_recursion
from graph_algorithms.dfs.contains_circle import contains_circle

from graph_algorithms.exception.graph_exception import GraphContainsCircleException
from graph_algorithms.exception.messages import sorting_not_possible_message


class _TopologicalSort(object):
    """The implementation topological sort."""

    def __init__(self):
        """Construct a new data structure."""
        self._sorted = []

    def pre_visit(self, vertex):
        """Doing nothing.

        Function called in explore function

        Args:
            vertex: vertex of graph
        """
        pass

    def post_visit(self, vertex):
        """Set vertex in sorted.

        Args:
            vertex: vertex of graph
        """
        self._sorted.append(vertex)

    @property
    def sorted(self):
        self._sorted.reverse()
        return self._sorted


def topological_sort(graph):
    """Return vertices in sorted.

    Args:
        graph: graph for sort

    Raises:
        GraphContainsCircleException: if graph contains circle

    Returns:
        sorted (list): vertices in sorted
    """
    if contains_circle(graph):
        raise GraphContainsCircleException(sorting_not_possible_message())
    sort = _TopologicalSort()
    dfs_recursion(graph, sort.pre_visit, sort.post_visit)
    return sort.sorted
