from tree_intersection import __version__
from tree_intersection.tree_intersection import tree_intersection,BinaryTree,Node
from tree_intersection.linkedList import Node,LinkedList
def test_version():
    assert __version__ == '0.1.0'


def test_tree_intersection():
    tree1=BinaryTree()
    tree1.root=Node('10')
    tree1.root.left=Node('20')
    tree1.root.right=Node('30')
    tree1.root.left.left=Node('40')
    tree1.root.left.right=Node('50')
    tree1.root.right.left=Node('60')

    tree2=BinaryTree()
    tree2.root=Node('10')
    tree2.root.left=Node('20')
    tree2.root.right=Node('25')
    tree2.root.left.left=Node('40')
    tree2.root.left.right=Node('80')
    tree2.root.right.left=Node('60')


    excepted = [10, 20, 40, 60]
    actual  = tree_intersection(tree1,tree2 )

    assert actual == excepted
