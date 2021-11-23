from tree_fizz_buzz import __version__
from tree_fizz_buzz.tree_fizz_buzz import tree_fizz_buzz,BinaryTree,Node

import pytest
def test_version():
    assert __version__ == '0.1.0'


def test_tree_breadth_first(create_tree):

    expected = "3-5-15-13-20-17-16-"
    actual=create_tree.tree_breadth_first(create_tree.root)
    assert actual == expected

def test_tree_fizz_buzz(create_tree):
    
    expected = ['Fizz', 'Buzz', 'FizzBuzz', '13', 'Buzz', '17', '16']
    tree = create_tree.tree_breadth_first(create_tree.root)
    actual = tree_fizz_buzz(tree)

    assert expected == actual


@pytest.fixture

def create_tree():
    tree = BinaryTree(3)
    tree.root.left = Node(5)
    tree.root.center = Node(15)
    tree.root.right = Node(13)
    tree.root.left.left = Node(20)
    tree.root.left.center= Node(17)
    tree.root.left.right = Node(16)
    return tree
