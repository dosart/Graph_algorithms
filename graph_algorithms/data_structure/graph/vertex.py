# -*- coding:utf-8 -*-

"""Implementation of  vertex for graph."""

from graph_algorithms.exception.graph_exception import NotContainsVertexException
from graph_algorithms.exception.messages import not_contains_vertex_message


class Vertex(object):
    """Class implements vertex for graph."""

    def __init__(self, identifier):
        """
        Construct a new vertex for graph.

        Args:
            identifier: vertex identifier
        """
        self._identifier = identifier
        self._adjacency_list = {}

    @property
    def identifier(self):
        """Return vertex's id.

        Returns:
            _identifier: unique id vertex in graph
        """
        return self._identifier

    @property
    def adjacency_list(self):
        """Return the name of adjacent vertices.

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

    def edge_weight_to(self, vertex):
        """Return  edge weight to vertex.

        Args:
            vertex: edge from self to vertex

        Raises:
             NotContainsVertexException: if vertex not contains in adjacency list

        Returns:
            weight (int) edge weight from self to vertex
        """
        if vertex not in self:
            raise NotContainsVertexException(not_contains_vertex_message(vertex.identifier))
        return self._adjacency_list[vertex]
    
    def __contains__(self, other):
        """Return  True if vertex contains in adjacency list.

        Args:
            other: vertex for search

        Returns:
            result (bool): True if vertex contains in adjacency list
        """
        for vertex in self._adjacency_list.keys():
            if vertex.identifier == other.identifier:
                return True
        return False

    def __str__(self):
        """Return string representation of vertex.

        Returns:
            str (string): string representation of vertex
        """
        return str(self._identifier)

    def __iter__(self):
        """Return iterator by adjacency list.

        Returns:
            iter (list iterator): iterator by adjacency list
        """
        return iter(self._adjacency_list.keys())
