# -*- coding:utf-8 -*-

"""Messages for Exception."""


def contains_circle_message():
    """Return message for GraphContainsCircleException.

    Returns:
        message: (str) message for exception
    """
    return 'Graph contains circle.'


def sorting_not_possible_message():
    """Return message for topological sort.

    Returns:
        message (str) message for exception
    """
    return 'Sorting is not possible. Graph contains circle.'


def graph_is_empty_message():
    """Return message for GraphIsEmptyException.

    Returns:
        message (str) message for exception
    """
    return 'Graph is empty.'


def graph_contains_vertex_message(vertex_id):
    """Return message for GraphContainsVertexExemption.

    Args:
       vertex_id: identifier of vertex

    Returns:
        message: (str) message for exception
    """
    return '{0} contains in graph'.format(vertex_id)


def not_contains_vertex_message(vertex_id):
    """Return message for GraphContainsVertexExemption.

    Args:
        vertex_id: identifier of vertex

    Returns:
        message: (str) message for exception
    """
    return '{0} not contains'.format(vertex_id)
