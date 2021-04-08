"""Implementation recursion depth-first search."""

from algorithms.dfs.explore import explore


def dfs_recursion(graph, pre_visit, post_visit):
    """Visit all the vertex of graph.

    Args:
        graph: graph for search
        pre_visit (function): сalled before vertex processing
        post_visit (function): сalled after vertex processing

    Returns:
        visited (dict): key (vertex id), value (true if vetrex is visited)
    """
    visited = {vertex.identifier: False for vertex in graph}

    for vertex in graph:
        if visited[vertex.identifier] is False:
            explore(vertex, visited, pre_visit, post_visit)
    return visited
