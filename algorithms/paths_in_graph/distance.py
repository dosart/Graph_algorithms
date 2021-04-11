"""Implementation of a collection to store the distance from the starting vertex to the rest in the graph.

The collection stores items:
    - key: vertex-identifier
    - value: disatance

Doesn't check if a key is contained in a collection.
"""

import sys


def make_distances(graph):
    """Return collection.

    Args:
        graph: graph for construct collection

    Returns:
        distance: collection (key:vertex-identifier, value:disatance)
    """
    return {vertex.identifier: None for vertex in graph}


def set_distance(vertex, distance, distances):
    """Set distance for vertex.

    Args:
        vertex: vertex for added
        distance: distance to the vertex
        distances: distance storage collection
    """
    distances[vertex.identifier] = distance


def get_distance(vertex, distances):
    """Return distance to vertex.

    Args:
        vertex: vertex to get distance
        distances: distance storage collection

    Returns:
        distance (int): distance to vertex
    """
    return distances[vertex.identifier]


def to_int(distance):
    """Convert None to sys.maxsize.

    Args:
        distance: distance for convert

    Returns:
        disatance: if disatance == None then return sys.maxsize else distance
    """
    if distance is None:
        return sys.maxsize
    return distance


def not_visited(vertex, distances):
    """Return true if vertex not visited.

    Args:
        vertex: vertex to get result
        distances: distance storage collection

    Returns:
        result (bool): true if vertex not visited
    """
    return True if distances[vertex.identifier] is None else False
