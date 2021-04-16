# -*- coding:utf-8 -*-

"""Tests of  algorithm depth first search."""

import pytest

from graph_algorithms.data_structure.graph.graph import Graph
from graph_algorithms.algorithms.dfs.dfs_recursion import dfs_recursion
from graph_algorithms.algorithms.dfs.dfs_iterative import dfs_iterative


def test_all_vertex_visited_dfs_iterative1():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')
    graph.create_vertex_by_id('E')

    # first component of connectivity
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'A')

    # second component of connectivity
    graph.add_edge('D', 'E')

    # third component of connectivity
    graph.create_vertex_by_id('K')

    visited = dfs_iterative(graph)

    assert all(value == True for value in visited.values())


def test_all_vertex_visited_dfs_iterative2():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')
    graph.create_vertex_by_id('E')

    visited = dfs_iterative(graph)

    assert all(value == True for value in visited.values())


def pre_visit(vertex):
    pass


def post_visit(vertex):
    pass


def test_all_vertex_visited_dfs_recursion1():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('C', 'C')

    visited = dfs_recursion(graph, pre_visit, post_visit)

    assert all(value == True for value in visited.values())


def test_all_vertex_visited_dfs_recursion2():
    graph = Graph()

    graph.create_vertex_by_id('A')
    graph.create_vertex_by_id('B')
    graph.create_vertex_by_id('C')
    graph.create_vertex_by_id('D')

    graph.add_edge('A', 'C')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')

    visited = dfs_recursion(graph, pre_visit, post_visit)

    assert all(value == True for value in visited.values())
