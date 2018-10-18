from random import randint


class Graph(object):

    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []

    def add_node(self, node):
        """Add node to the graph if node is not present.
        :param node: {Node}
        """
        if node not in self.nodes:
            self.nodes.append(node)


class Node(object):

    def __init__(self, id=None):
        self.id = id or randint(0,100)

    def __eq__(self, other):
        return self.id == other.id


