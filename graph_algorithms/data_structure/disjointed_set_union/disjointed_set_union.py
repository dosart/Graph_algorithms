# -*- coding:utf-8 -*-
"""Disjoint-set-union implementation."""

import secrets


class DSU(object):
    """Class implements disjoint-set-union data structure."""

    def __init__(self):
        """Construct a new DSU."""
        self._set = {}

    def make_set(self, vertex):
        """Construct new singleton set.

        Args:
            vertex: element of new set
        """
        # key: vertex
        # value: parent(vertex)
        self._set[vertex] = vertex

    def find(self, vertex):
        """Return unique id of set.

        Args:
            vertex: element for search id

        Returns:
            id: unique set identifier found by arg
        """
        if self._set[vertex] == vertex:
            return vertex
        self._set[vertex] = self.find(self._set[vertex])
        return self._set[vertex]

    def unite(self, vertex_x, vertex_y):
        """Combine the sets containing.

        Args:
            vertex_x: element first set
            vertex_y: element second set
        """
        parent_x = self.find(vertex_x)
        parent_y = self.find(vertex_y)

        if secrets.randbelow(10) % 2 == 0:
            self._set[parent_x] = parent_y
        else:
            self._set[parent_y] = parent_x
