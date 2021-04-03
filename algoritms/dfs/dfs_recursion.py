"""Implementation recursion depth-first search."""

from algoritms.explore import explore


def pre_visit(vertex):
    pass


def post_visit(vertex):
    pass


def dfs_recursion(graph):
    """Visit all the vertex of graph.

    Args:
        graph: graph for search

    Returns:
        visited (dict): key (vertex id), value (true if vetrex is visited)
    """
    visited = {vertex.identifier: False for vertex in graph}

    for vertex in graph:
        if visited[vertex.identifier] is False:
            explore(vertex, visited, pre_visit, post_visit)
    return visited
