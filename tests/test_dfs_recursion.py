"""Tests of  algorithm depth first search."""

from algoritms.graph import Graph
from algoritms.dfs_recursion import dfs_recursion


def test_all_vertex_visited():
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

    #third component of connectivity
    graph.create_vertex_by_id('K')

    visited = dfs_recursion(graph)

    assert all(value == True for value in visited.values())
