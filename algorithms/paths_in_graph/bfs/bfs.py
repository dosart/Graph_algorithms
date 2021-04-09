"""Implementation iterative breadth-first search."""

from collections import deque


def make_distances(graph):
    return {vertex: None for vertex in graph}


def set_distance(vertex, distance, distances):
    distances[vertex] = distance


def get_distance(vertex, distances):
    return distances[vertex]


def not_visited(vertex, distances):
    return True if distances[vertex] is None else False


def make_queue():
    return deque()


def enqueue(queue, element):
    queue.append(element)


def dequeue(queue):
    return queue.popleft()


def is_empty(queue):
    return len(queue) == 0


def bfs(graph, start_vertex):
    distances = make_distances(graph)
    set_distance(start_vertex, 0)

    vertices = make_queue()
    enqueue(vertices, start_vertex)

    while not is_empty(vertices):
        vertex = dequeue(vertices)
        for adjacent_vertex in vertex:
            if not_visited(adjacent_vertex, distances):
                enqueue(vertices, adjacent_vertex)
                set_distance(adjacent_vertex, distances,
                             get_distance(vertex) + 1)
    return distances
