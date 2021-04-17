# -*- coding:utf-8 -*-

"""Tests of disjoint-set-union."""

import pytest

from graph_algorithms.data_structure.disjointed_set_union.disjointed_set_union import DSU


def test_find():
    s = DSU()

    s.make_set(1)
    s.make_set(2)
    s.make_set(3)
    s.make_set(4)

    assert s.find(1) == 1
    assert s.find(2) == 2
    assert s.find(3) == 3
    assert s.find(4) == 4


def test_unite1():
    s = DSU()

    s.make_set(1)
    s.make_set(2)
    s.make_set(3)
    s.make_set(4)
    s.make_set(5)

    s.unite(1, 4)
    s.unite(3, 5)

    assert s.find(1) == s.find(4)
    assert s.find(5) == s.find(5)
    assert s.find(2) == 2


def test_unite2():
    s = DSU()

    s.make_set(2)
    s.make_set(4)
    s.make_set(6)
    s.make_set(8)
    s.make_set(10)

    s.unite(2, 4)
    s.unite(6, 8)

    assert s.find(2) == s.find(4)
    assert s.find(6) == s.find(8)

    s.unite(8, 2)

    assert s.find(2) == s.find(8)
    assert s.find(2) == s.find(4)
    assert s.find(2) == s.find(6)

    s.unite(6, 10)
    assert s.find(2) == s.find(8)
    assert s.find(2) == s.find(4)
    assert s.find(2) == s.find(6)
    assert s.find(2) == s.find(10)
