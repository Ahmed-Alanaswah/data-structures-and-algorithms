class Node(object):
    def __init__(self,value=None):
        self.value= value
        self.left = None
        self.right =None



class BinaryTree(object):
    def __init__(self,root) :
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root,"")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root,"")
        else:
            print("traversal type " + str(traversal_type)+  " is not supported ")
            return False
    def preorder_print(self,start,traversal):
        """"root->left->right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal
    def inorder_print(self,start,traversal):
        """left -> root -> right """
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right,traversal)
        return traversal
    def postorder_print(self,start,traversal):
        """"left->right ->root"""
        if start:
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
            traversal += (str(start.value) + "-")
        return traversal






class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value,cur_node.left)

        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value,cur_node.right)

        else:
            print("value is  already present in tree")

    def find(self,value):
        if self.root:
            is_found = self._find(value,self.root)

            if is_found:
                return True
            else:
                return False

        return None

    def _find(self,value,cur_node):
        if value > cur_node.value and cur_node.right:
            return self._find(value,cur_node.right)
        elif value < cur_node.value and cur_node.left:
            self._find(value,cur_node.left)

        if value == cur_node.value :
            return True



tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print("============")
bst = BinarySearchTree()

bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
print(bst.find(12))

# class Tree:
#     def __init__(self):
#         self.root = None
     
#     def pre_order(self):
#         output=[]
        
#         def _traverses(_root):
#             output.append(_root.value)
#             if _root.left is not None:
#                 _traverses(_root.left)
#             if _root.right is not None:
#                  _traverses(_root.right)
#             return output
#         return _traverses

# def create_tree():
#     tree=Tree()
#     tree.root=Node("A") 
#     tree.root.left=Node("B") 
#     tree.root.right=Node("C") 
#     tree.root.left.left=Node("D") 
#     tree.root.left.right=Node("E") 
#     tree.root.right.left=Node("F") 
#     return tree

# if __name__=="__main__":
#     tree=create_tree()
#     traverses = tree.pre_order()
#     print(traverses(tree.root))