"""Algorithm for visiting vertices of a connected component."""


def explore(vertex, visited, pre_visit, post_visit):
    """Find all vertices reachable from a arg.

    Args:
        vertex: start vertex for explore
        visited (dict): key (vertex id), value (true if vetrex is visited)
    """
    visited[vertex.identifier] = True

    pre_visit(vertex)

    for adjacent_vertex in vertex:
        if visited[adjacent_vertex.identifier] is False:
            explore(adjacent_vertex, visited, pre_visit, post_visit)
    
    post_visit(vertex)
