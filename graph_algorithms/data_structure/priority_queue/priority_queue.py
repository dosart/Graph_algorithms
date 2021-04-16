# -*- coding:utf-8 -*-

"""Implementation priority queue.

Private data structure. Only for search algorithms.
"""

from graph_algorithms.data_structure.priority_queue.heapdict.heapdict import heapdict

import sys


def make_priority_queue(graph):
    """Construct new priority queue from graph.

    Args:
        graph: source to create the priority queue

    Returns:
        heep: priority queue
    """
    heep = heapdict()
    for vertex in graph:
        heep[vertex] = sys.maxsize
    return heep


def set_priority(vertex, priority, heap):
    """Set priority for vertex.

    Args:
        vertex: vertex for setting priority
        priority (int): priority
        heap: priority queue
    """
    heap[vertex] = priority


def extract_min(heap):
    """Extract vertex with minimum priority.

    Args:
        heap: priority queue

    Returns:
        vertex: vertex with minimum priority
    """
    vertex, priority = heap.popitem()
    return vertex


def decrease_priority(vertex, new_priority, heap):
    """Decrease priority for vertex.

    Args:
        vertex: vertex for decrease priority
        new_priority: new priority for vertex
        heap: priority queue
    """
    heap[vertex] = new_priority


def is_empty(heap):
    """Return true if heeap is empty.

    Args:
        heap: priority queue

    Returns:
        result (bool): true if heeap is empty
    """
    return len(heap) == 0
