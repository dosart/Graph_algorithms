# -*- coding:utf-8 -*-

"""Tests of  algorithm topological sort."""

import pytest

from graph_algorithms.algorithms.dfs.topological_sort import topological_sort as dfs_topological_sort
from graph_algorithms.algorithms.topological_sort import topological_sort
from graph_algorithms.data_structure.graph.graph import Graph


def test_topological_sort1():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('G')
    graph.create_vertex_by_id('D')
    graph.create_vertex_by_id('E')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'G')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('B', 'D')
    graph.add_edge('G', 'D')
    graph.add_edge('D', 'E')

    result = dfs_topological_sort(graph)
    assert result[0].identifier == 'A'
    assert result[1].identifier == 'G'
    assert result[2].identifier == 'B'
    assert result[3].identifier == 'C'
    assert result[4].identifier == 'D'
    assert result[5].identifier == 'E'


def test_topological_sort2():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('G')
    graph.create_vertex_by_id('D')
    graph.create_vertex_by_id('E')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'G')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('B', 'D')
    graph.add_edge('G', 'D')
    graph.add_edge('D', 'E')

    result = topological_sort(graph)
    assert result[0].identifier == 'A'
    assert result[1].identifier == 'B'
    assert result[2].identifier == 'G'
    assert result[3].identifier == 'C'
    assert result[4].identifier == 'D'
    assert result[5].identifier == 'E'


@pytest.mark.parametrize("sort", [dfs_topological_sort, topological_sort])
def test_topological_sort3(sort):
    graph = Graph()

    graph.create_vertex_by_id('A')

    result = sort(graph)

    assert result[0].identifier == 'A'
