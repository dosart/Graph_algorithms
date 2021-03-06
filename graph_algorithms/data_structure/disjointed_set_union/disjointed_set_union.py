# -*- coding:utf-8 -*-
"""Disjoint-set-union implementation."""

import secrets

from graph_algorithms.exception.graph_exception import NotContainsElementException
from graph_algorithms.exception.messages import not_contains_element_message

from graph_algorithms.exception.graph_exception import DataStructureIsEmptyException
from graph_algorithms.exception.messages import data_structure_is_empty_message


class DSU(object):
    """Class implements disjoint-set-union data structure."""

    def __init__(self):
        """Construct a new DSU."""
        self._set = {}

    @property
    def size(self):
        """Return size of data structure.

        Returns:
            size(int) size of data structure

        """
        return len(self._set)

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

        Raises:
            NotContainsElementException: if dsu not contains vertex
            DataStructureIsEmptyException: if dsu is empty

        Returns:
            id: unique set identifier found by arg
        """
        if self.size == 0:
            raise DataStructureIsEmptyException(data_structure_is_empty_message())
        if vertex not in self._set:
            raise NotContainsElementException(not_contains_element_message())
        if self._set[vertex] == vertex:
            return vertex
        self._set[vertex] = self.find(self._set[vertex])
        return self._set[vertex]

    def unite(self, vertex_x, vertex_y):
        """Combine the sets containing.

        Args:
            vertex_x: element first set
            vertex_y: element second set

        Raises:
            NotContainsElementException: if dsu not contains vertex
            DataStructureIsEmptyException: if dsu is empty
        """
        if self.size == 0:
            raise DataStructureIsEmptyException(data_structure_is_empty_message())
        if vertex_x not in self._set:
            raise NotContainsElementException(not_contains_element_message())
        if vertex_y not in self._set:
            raise NotContainsElementException(not_contains_element_message())

        parent_x = self.find(vertex_x)
        parent_y = self.find(vertex_y)

        if secrets.randbelow(10) % 2 == 0:
            self._set[parent_x] = parent_y
        else:
            self._set[parent_y] = parent_x

    def __len__(self):
        """Return size of dsu.

        Returns:
            size (int): size of dsu
        """
        return self.size
