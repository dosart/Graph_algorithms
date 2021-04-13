"""Implementation of  edge for graph."""


class Edge(object):
    """Class implements edge for graph."""

    def __init__(self, first_vertex, second_vertex, weight=0):
        """Construct a new edge for graph.

        Args:
            first_vertex: first vertex id of edge
            second_vertex: second vertex id of edge
            weight (int): weight (cost) of edge
        """
        self._first_vertex_id = first_vertex
        self._second_vertex_id = second_vertex
        self._weight = weight

    @property
    def first(self):
        """Return first vertex of edge.

        Returns:
            first: first vertex id of edge
        """
        return self._first_vertex_id

    @property
    def second(self):
        """Return second vertex of edge.

        Returns:
            second : second vertex id of edge
        """
        return self._second_vertex_id

    @property
    def weight(self):
        """Return weight vertex of edge.

        Returns:
            weight (int): weight (cost) of edge
        """
        return self._weight
