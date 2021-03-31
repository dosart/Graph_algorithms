"""Implementation iterative depth-first search."""


def dfs_iterative(graph):
    """Visit all the vertex of graph.

    Args:
        graph: graph for search

    Returns:
        visited (dict): key (vertex id), value (true if vetrex is visited)
    """
    visited = {vertex : False for vertex in graph}

    stack = []
    for vertex in graph:
        stack.append(vertex)

    while len(stack) > 0:
        vertex = stack.pop()
        for adjacent_vertex in vertex:
            if visited[adjacent_vertex] is False:
                  stack.append(adjacent_vertex)
                  visited[adjacent_vertex] == True
    return visited
