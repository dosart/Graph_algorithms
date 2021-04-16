"""Implementation relax function.

The function gets the edge (u, v) of the graph and and tries to improve the distance to v
"""

from graph_algorithms.paths_in_graph.distance import get_distance
from graph_algorithms.paths_in_graph.distance import set_distance
from graph_algorithms.paths_in_graph.distance import number


def relax(first_vertex, second_vertex, distance):
    """Relax edge between first vertex and second vertex.

    Args:
        first_vertex: first vertex of edge
        second_vertex: second vertex of edge
        distance: list of distances of vertices

    Returns:
        result (bool): return True if edge relaxed
    """
    weight = edge_weight(first_vertex, second_vertex, distance)
    if _get_distance(second_vertex, distance) > weight:
        set_distance(second_vertex, weight, distance)
        return True
    return False


def edge_weight(first_vertex, second_vertex, distance):
    """Return weight of edge.

    Args:
        first_vertex: first vertex of edge
        second_vertex: second vertex of edge
        distance: data structure for distances of vertices graph

    Returns:
        weight (int): weight of edge
    """
    return number(get_distance(first_vertex, distance)) + first_vertex.edge_weight_to(second_vertex)


def _get_distance(vertex, distance):
    return number(get_distance(vertex, distance))
