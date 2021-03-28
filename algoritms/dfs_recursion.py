"""Implementation recursion depth-first search."""

from algoritms.graph import Graph
from algoritms.vertex import Vertex


def explore(vertex, visited):
    """Finding all vertices reachable from a arg.

    Args:
        vertex: start vertex for explore
        visited (dict): key (vertex id), value (true if vetrex is visited)
    """
    visited[vertex.id] = True

    for adjacent_vertex in vertex:
        if visited[adjacent_vertex.id] == False:
            explore(adjacent_vertex, visited)


def dfs_recursion(graph):
    """Implementation recursion depth-first search.
    
    Returns:
        visited (dict): key (vertex id), value (true if vetrex is visited)
    """
    visited = {vertex.id: False for vertex in graph}

    for vertex in graph:
        if visited[vertex.id] == False:
            explore(vertex, visited)
    return visited
