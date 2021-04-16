# -*- coding:utf-8 -*-

"""Implementation simple queue for breadth-first search.

Private data structure. Only for BFS.
"""

from collections import deque


def make_queue():
    """Make and return queue.

    Returns:
        queue: simple queue
    """
    return deque()


def enqueue(queue, element):
    """Add element in queue.

    Args:
        queue: simple queue
        element: element to added
    """
    queue.append(element)


def dequeue(queue):
    """Return first element from queue.

    Args:
        queue: simple queue

    Returns:
        element: first element from queue
    """
    return queue.popleft()


def is_empty(queue):
    """Return true if queue is empty.

    Args:
        queue: simple queue

    Returns:
        result (bool): true if queue is empty
    """
    return len(queue) == 0
