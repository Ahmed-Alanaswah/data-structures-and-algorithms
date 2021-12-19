from graph import __version__

from graph.graph import Graph
def test_version():
    assert __version__ == '0.1.0'


def test_breadth_first():
    graph=Graph()
    val1=graph.add_node("A")
    val2=graph.add_node("B")
    val3=graph.add_node("C")
    graph.add_edge(val1,val2,50)
    graph.add_edge(val1,val3,1)
    graph.add_edge(val2,val3,1)
    actual = graph.breadth_first(val1)
    expected = ['A', 'B', 'C']
    assert actual == expected
