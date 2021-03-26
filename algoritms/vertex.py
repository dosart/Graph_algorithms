"""Implementation of  vertex for graph."""


class Vertex(object):
    """Class implements vertex for graph."""

    def __init__(self, name):
        """
        Construct a new vertex for graph.

        Args:
            name: vertex id
        """
        self._name = name
        self._adjacency_list = {}

    @property
    def adjacency_list(self):
        """Return  adjacency list of vertex.

        Returns:
            list (list): adjacency list of vertex
        """
        return self._adjacency_list.keys()

    def add_adjacent_vertex(self, vertex, weight=0):
        """Add vertex in adjacency list of vertex.

        Args:
            vertex: vertex for add
            weight (int): weight of edge
        """
        self._adjacency_list[vertex] = weight

    def __str__(self):
        """Return string representation of vertex.

        Returns:
            str (string): string representation of vertex
        """
        return str(self._name)
