# -*- coding:utf-8 -*-

"""Tests of algorithm for calculating the components of graph connectivity."""

import pytest

from graph_algorithms.data_structure.graph.graph import Graph
from graph_algorithms.algorithms.dfs.connected_components import connected_components


def test_one_component():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')

    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')

    components = connected_components(graph)

    assert components['A'] == 1
    assert components['B'] == 1
    assert components['C'] == 1


def test_two_component():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')

    graph.add_edge('A', 'B')
    graph.add_edge('C', 'D')

    components = connected_components(graph)

    assert components['A'] == 1
    assert components['B'] == 1
    assert components['C'] == 2
    assert components['D'] == 2


def test_four_component():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')

    components = connected_components(graph)

    assert components['A'] == 1
    assert components['B'] == 2
    assert components['C'] == 3
    assert components['D'] == 4
