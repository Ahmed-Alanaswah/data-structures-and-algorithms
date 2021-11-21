
from tree_max import __version__
from tree_max.tree_max import BinaryTree,Node


def test_version():
    assert __version__ == '0.1.0'
def test_max_value():
        tree=BinaryTree(1)
        tree.root.left=Node(2)
        tree.root.right=Node(3)
        tree.root.left.left=Node(4)
        tree.root.left.right=Node(5)
        tree.root.right.left=Node(6)
        tree.root.right.right=Node(7)

        expected = 7
        actual = tree.maximum_value(tree.root)
        assert actual == expected