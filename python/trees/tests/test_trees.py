from trees import __version__
from trees.trees import BinaryTree,BinarySearchTree,Node
import pytest 
def test_version():
    assert __version__ == '0.1.0'

#      A
#  B        c 
# D E       f


def test_pre_oder(create_tree):

    expected = "1-2-4-5-3-6-7-"
    assert create_tree.preorder_print(create_tree.root,"") == expected


def test_in_oder(create_tree):

    expected = "4-2-5-1-6-3-7-"
    assert create_tree.inorder_print(create_tree.root,"") == expected

def test_post_oder(create_tree):

    expected = "2-4-5-3-6-7-1-"
    assert create_tree.postorder_print(create_tree.root,"") == expected


def test_Find():
        bst=BinarySearchTree()
        bst.insert(4)
        bst.insert(2)
        bst.insert(8)
        bst.insert(5)
        bst.insert(10)
        actual = bst.find(10)
        expected = True
        assert actual == expected


def test_empty_b():
        bst=BinarySearchTree()
        
        actual =bst.insert(4)
        expected = None
        assert actual == expected



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

