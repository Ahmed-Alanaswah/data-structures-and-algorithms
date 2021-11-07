# from linked_list import __version__
from linked_list.linked_list import LinkedList,Node
import pytest

# def test_version():
#     assert __version__ == "0.1.0"


def test_emty_linked_list():
    ll=LinkedList()
    expected=None
    actual=ll.head
    assert expected==actual

def test_appen3_values(ll):
  
    expected = "head -> 5 -> hello -> 1.57 -> None" 
    actual = ll.__str__()
    assert expected == actual

def test_append_to_existing_ll(ll):
    ll.append(True)
    expected="head -> 5 -> hello -> 1.57 -> True -> None"
    actual = ll.__str__()
    assert expected == actual

@pytest.fixture
def ll():
    ll=LinkedList()
    ll.append(5) 
    ll.append('hello') 
    ll.append(1.57)
    return ll 
