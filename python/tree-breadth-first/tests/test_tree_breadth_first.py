from tree_breadth_first import __version__
from tree_breadth_first.tree_breadth_first import BinaryTree,Node
import pytest
def test_version():
    assert __version__ == '0.1.0'


def test_tree_breadth_first(create_tree):

    expected = "1-2-3-4-5-6-7-"
    assert create_tree.tree_breadth_first(create_tree.root) == expected


    
@pytest.fixture

def create_tree():
    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    return tree