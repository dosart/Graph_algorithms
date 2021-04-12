# -*- coding:utf-8 -*-

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
