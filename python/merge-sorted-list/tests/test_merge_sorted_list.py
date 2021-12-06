from merge_sorted_list import __version__
from merge_sorted_list.merge_sorted_list import Mergesort

def test_version():
    assert __version__ == '0.1.0'


def test_list():
    arr = [8,4,23,42,16,15]
    actual = Mergesort(arr)
    expected = [4, 8, 15, 16, 23, 42] 
    assert actual == expected


def test_reversed_list():
    arr = [20,18,12,8,5,-2]
    actual = Mergesort(arr)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected



def test_unique_list():
    arr = [5,12,7,5,5,7]
    actual = Mergesort(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_sorted_list():
    arr = [2,3,5,7,13,11]
    actual = Mergesort(arr)
    expected = [2, 3, 5, 7, 11, 13] 
    assert actual == expected