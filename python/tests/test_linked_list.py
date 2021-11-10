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

def test_insert_to_existing_ll(ll):
    ll.insert(1)
    expected="head -> 1 -> 5 -> hello -> 1.57 -> None"
    actual = ll.__str__()
    assert expected == actual

def test_include_to_existing_ll(ll):
    ll.include(5)
    expected=True
    actual = ll.include(5)
    assert expected == actual

def test_notinclude_to_existing_ll(ll):
    ll.include(10)
    expected=False
    actual = ll.include(10)
    assert expected == actual

def test_addBefore5_to_existing_ll(ll):
    ll.addBefor("b",5)
    expected="head -> b -> 5 -> hello -> 1.57 -> None" 
    actual =ll.__str__()
    assert expected == actual

def test_addBeforehello_to_existing_ll(ll):
    ll.addBefor("b","hello")
    expected="head -> 5 -> b -> hello -> 1.57 -> None" 
    actual =ll.__str__()
    assert expected == actual


def test_addafter5_to_existing_ll(ll):
    ll.addAfter("b",5)
    expected="head -> 5 -> b -> hello -> 1.57 -> None" 
    actual =ll.__str__()
    assert expected == actual

def test_addafterhello_to_existing_ll(ll):
    ll.addAfter("b","hello")
    expected="head -> 5 -> hello -> b -> 1.57 -> None" 
    actual =ll.__str__()
    assert expected == actual

def test_printNthFromLast_to_existing_ll(ll):
    ll.printNthFromLast(1)
    expected=1.57
    actual =ll.printNthFromLast(1)
    assert expected == actual


def test_ziplist(ll,ll2):
    ll.ziplist(ll,ll2)
    expected="head -> 5 -> 1 -> hello -> 2 -> 1.57 -> 3 -> None"
    actual =ll.__str__()
    assert expected == actual

@pytest.fixture
def ll():
    ll=LinkedList()
    ll.append(5) 
    ll.append('hello') 
    ll.append(1.57)
   
    return ll
@pytest.fixture
def ll2():
    ll2=LinkedList()
    ll2.append(1) 
    ll2.append(2) 
    ll2.append(3)
   
    return ll2 