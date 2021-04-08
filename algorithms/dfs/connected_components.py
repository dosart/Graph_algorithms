"""Implementation of the algorithm for calculating the components of graph connectivity."""

from algorithms.dfs.explore import explore


class _ConnectedComponents(object):
    """The class counts the connected components of the graph."""

    def __init__(self, count=1):
        """Construct a new connected components data structure.

        Args:
            count (int): the initial value of the counter
        """
        self._components = {}
        self._count = count

    @property
    def components(self):
        """Return the number connected components.

        Returns:
            components (dict): key (vertex id), value (connectivity component number)
        """
        return self._components

    def inc_count(self):
        """Increment count the connected components."""
        self._count += 1

    def pre_visit(self, vertex):
        """Set number of the connected component for vertex.

        Function called in explore function

        Args:
            vertex: vertex of graph
        """
        self._components[vertex.identifier] = self._count

    def post_visit(self, vertex):
        """Doing nothing.

        Function called in explore function

        Args:
            vertex: vertex of graph
        """
        pass


def connected_components(graph):
    """Return the number connected components.

       Args:
            graph: graph for calculating connectivity components

       Returns:
            components (dict): key (vertex id), value (connectivity component number)
    """
    visited = {vertex.identifier: False for vertex in graph}
    components = _ConnectedComponents()

    for vertex in graph:
        if visited[vertex.identifier] is False:
            explore(vertex, visited, components.pre_visit, components.post_visit)
            components.inc_count()
    return components.components
