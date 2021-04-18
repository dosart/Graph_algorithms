# -*- coding:utf-8 -*-

"""Vertex data structure tests."""

import pytest

from graph_algorithms.data_structure.graph.vertex import Vertex

from graph_algorithms.exception.graph_exception import NotContainsVertexException
from graph_algorithms.exception.messages import not_contains_vertex_message


def test_edge_weight_to_negative():
    vertex_s = Vertex('S')
    vertex_a = Vertex('A')
    vertex_b = Vertex('B')

    vertex_s.add_adjacent_vertex(vertex_a)

    with pytest.raises(NotContainsVertexException) as exception_info:
        weight = vertex_s.edge_weight_to(vertex_b)

    assert str(exception_info.value) == not_contains_vertex_message('B')


def test_edge_weight_to_positive():
    vertex_s = Vertex('S')
    vertex_a = Vertex('A')

    vertex_s.add_adjacent_vertex(vertex_a, 5)

    weight = vertex_s.edge_weight_to(vertex_a)

    assert weight == 5


def test_vertex_str1():
    vertex = Vertex('A')

    assert str(vertex) == 'A'


def test_vertex_str2():
    vertex = Vertex(1)

    assert str(vertex) == '1'
