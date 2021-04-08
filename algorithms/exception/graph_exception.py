"""Exceptions of graphs."""


class GraphContainsVertexExemption(Exception):
    """Exception class if a graph contains vertex."""

    pass  # noqa: WPS420, WPS604


class GraphIsEmptyException(Exception):
    """Exception class if a graph is empty."""

    pass  # noqa: WPS420, WPS604


class GraphNotContainsVertexException(Exception):
    """Exception class if a graph contains vertex."""

    pass  # noqa: WPS420, WPS604


class GraphContainsCircleException(Exception):
    """Exception class if a graph contains circle."""

    pass  # noqa: WPS420, WPS604


def contains_circle_message():
    """Return message for GraphContainsCircleException.

    Returns:
        message (str) message for exeption
    """
    return 'Graph contains circle.'


def sorting_not_possible_message():
    """Return message for topological sort.

    Returns:
        message (str) message for exeption
    """
    return 'Sorting is not possible. Graph contains circle.'
