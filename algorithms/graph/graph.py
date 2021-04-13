# -*- coding:utf-8 -*-

"""Graph data structure implementation."""

from algorithms.graph.vertex import Vertex

from algorithms.exception.graph_exception import GraphContainsVertexExemption
from algorithms.exception.graph_exception import NotContainsVertexException
from algorithms.exception.graph_exception import GraphIsEmptyException
from algorithms.exception.messages import graph_is_empty_message
from algorithms.exception.messages import not_contains_vertex_message
from algorithms.exception.messages import graph_contains_vertex_message


class Graph(object):
    """Class implements graph data structure."""

    def __init__(self):
        """Construct a new graph data structure."""
        self._vertices = {}

    def __contains__(self, vertex_id):
        """Return true if vertex_id contains in graph.

        Args:
            vertex_id: unique id of the vertex in the graph

        Returns:
            result (bool): true if vertex_id contains in graph
        """
        return vertex_id in self._vertices

    def __len__(self):
        """Return size of graph.

        Returns:
            size (int): size of grapg
        """
        return self.size

    @property
    def size(self):
        """Return number of vertices of graph.

        Returns:
            size (int): size of grapg
        """
        return len(self._vertices)

    @property
    def is_empty(self):
        """Return true if graph is empty (number of vertices == 0).

        Returns:
            result (bool): true if graph is empty else false
        """
        return self.size == 0

    def create_vertex_by_id(self, vertex_id):
        """Create vertex in graph.

        Args:
            vertex_id: unique vertex id

        Raises:
            GraphContainsVertexExemption: if graph contains vertex
        """
        if vertex_id in self._vertices:
            raise GraphContainsVertexExemption(graph_contains_vertex_message(vertex_id))
        self._vertices[vertex_id] = Vertex(vertex_id)

    def get_vertex_by_id(self, vertex_id):
        """Return (not extract) vertex from graph.

        Args:
            vertex_id: vertex for return

        Returns:
            vertex: vertex by id

        Raises:
            GraphIsEmptyException: if graph is empty
            NotContainsVertexException: if graph not contains vertex
        """
        if self.is_empty:
            raise GraphIsEmptyException(graph_is_empty_message())
        if vertex_id not in self._vertices:
            raise NotContainsVertexException(not_contains_vertex_message(vertex_id))
        return self._vertices[vertex_id]

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Add an edge between two vertices.

        Args:
            from_vertex: start vertex id
            to_vertex: end vertex id
            weight (int): weight of edge

        Raises:
            GraphIsEmptyException: if graph is empty
            NotContainsVertexException: if vertex not contains in graph
        """
        if self.is_empty:
            raise GraphIsEmptyException(graph_is_empty_message())
        if from_vertex not in self._vertices:
            raise NotContainsVertexException(not_contains_vertex_message(from_vertex))
        if to_vertex not in self._vertices:
            raise NotContainsVertexException(not_contains_vertex_message(to_vertex))

        vertex = self._vertices[to_vertex]
        self._vertices[from_vertex].add_adjacent_vertex(vertex, weight)

    def __iter__(self):
        """Return iterator by vertices.

        Returns:
            iter (list iterator): iterator by vertices
        """
        return iter(self._vertices.values())
