"""Implementation recursion depth-first search."""

from algoritms.dfs.explore import explore


def _pre_visit(vertex):
    """Doing nothing.

       Function called in explore function

       Args:
            vertex: vertex of graph
    """
    pass


def _post_visit(vertex):
    """Doing nothing.

       Function called in explore function

       Args:
            vertex: vertex of graph
    """
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
            explore(vertex, visited, _pre_visit, _post_visit)
    return visited
