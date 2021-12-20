from graph import __version__
import pytest

from graph.graph import Graph, business_trip
def test_version():
    assert __version__ == '0.1.0'
 


@pytest.fixture()
def create_graph():
    graph = Graph()
    pandora = graph.add_node("Pandora")
    arendelle = graph.add_node("Arendelle")
    monstropolis = graph.add_node("Monstropolis")
    metroville = graph.add_node("Metroville")
    naboo = graph.add_node("Naboo")
    narnia = graph.add_node("Narnia")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)

    graph.add_edge(arendelle, pandora, 150)
    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(arendelle, metroville, 99)

    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(metroville, narnia, 37)

    graph.add_edge(monstropolis, arendelle, 42)
    graph.add_edge(monstropolis, metroville, 105)
    graph.add_edge(monstropolis, naboo, 73)

    graph.add_edge(naboo, metroville, 26)
    graph.add_edge(naboo, narnia, 250)
    graph.add_edge(naboo, monstropolis, 73)

    graph.add_edge(narnia, metroville, 37)
    graph.add_edge(narnia, naboo, 250)
    return graph

def test_graph_business_trip_two_citis_not_connected(create_graph):
    graph = create_graph

    expected = "False, $0"

    actual = business_trip(graph, ["Naboo", "Pandora"])

    assert actual == expected

    actual = business_trip(graph, ["Narnia", "Arendelle", "Naboo"])

    assert actual == "False, $0"


def test_graph_business_trip_three_cities(create_graph):
    graph = create_graph

    expected = "True, $115"

    actual = business_trip(graph, ["Arendelle", "Monstropolis", "Naboo"])

    assert actual == expected


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
