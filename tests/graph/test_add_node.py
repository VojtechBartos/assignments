from assignments.graph.graph import Graph, Node


def test_add_node():
    graph = Graph()
    graph.add_node(Node(1))
    assert len(graph.nodes) == 1
    graph.add_node(Node(2))
    assert len(graph.nodes) == 2
    graph.add_node(Node(2))
    assert len(graph.nodes) == 2