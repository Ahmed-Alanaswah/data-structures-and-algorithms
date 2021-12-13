
from linkedList import LinkedList,Node
from hashatable import HashTable

class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None
        self.output = []

    def pre_order(self, root):
        if root == None:
            return self.output

        self.output.append(root.value)
        if root.left != None:
            self.pre_order(root.left)
        if root.right != None:
            self.pre_order(root.right)
        
        return self.output


    def in_order(self,root):
        if root == None:
            return self.output

        if root.left is not None:
            self.in_order(root.left)
        
        self.output.append(root.value)

        if root.right is not None:
            self.in_order(root.right)
        
        return self.output
        

    def post_order(self,root):
        if root == None:
            return self.output
        
        if root.left is not None:
            self.post_order(root.left)
        
        if root.right is not None:
            self.post_order(root.right)
        
        self.output.append(root.value)
        
        return self.output


def tree_intersection(tree1,tree2 ):
    tree1 = tree1.pre_order(tree1.root)
    tree2= tree2.pre_order(tree2.root)
    hash_table=HashTable()
    dublicate = []
    for  i in  tree1 : 
        
        hash_table.add(i)
        
    for  j in  tree2 : 
        
        hash_table.add(j)


    for i in hash_table.map:
  
        if isinstance(i,LinkedList) :
            dublicate.append(int(i.head.value)) 
        
    print(dublicate)
    

tree1=BinaryTree()
tree1.root=Node('10')
tree1.root.left=Node('20')
tree1.root.right=Node('30')
tree1.root.left.left=Node('40')


tree2=BinaryTree()
tree2.root=Node('10')
tree2.root.left=Node('20')
tree2.root.right=Node('25')
tree2.root.left.left=Node('40')

print(tree1.pre_order(tree1.root))
print(tree2.pre_order(tree2.root))

print(tree_intersection(tree1,tree2 ))




