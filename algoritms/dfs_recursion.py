"""Implementation recursion depth-first search."""


def explore(vertex, visited):
    """Find all vertices reachable from a arg.

    Args:
        vertex: start vertex for explore
        visited (dict): key (vertex id), value (true if vetrex is visited)
    """
    visited[vertex.identifier] = True

    for adjacent_vertex in vertex:
        if visited[adjacent_vertex.identifier] is False:
            explore(adjacent_vertex, visited)


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
            explore(vertex, visited)
    return visited
