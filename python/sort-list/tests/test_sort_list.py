from sort_list import __version__
from sort_list.sort_list import SelectionSort

def test_version():
    assert __version__ == '0.1.0'



def test_sort_list():
    arr = [8,4,23,42,16,15]
    actual = SelectionSort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected 


def test_reverse_sorted_list():
    arr = [20,18,12,8,5,-2]
    actual = SelectionSort(arr)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected 


def test_Few_uniques_list():
    arr = [5,12,7,5,5,7]
    actual = SelectionSort(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected 


def test_sort_sorted_list():
    arr = [2,3,5,7,13,11]
    actual = SelectionSort(arr)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected 
