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

    
    def maximum_value(self, temp):  
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty");  
            return 0;  
              
        else:      
            #Variable maximum will store temp's data  
            maximum = temp.value;  
              
            #It will find largest element in left subtree  
            if(temp.left != None):  
                leftMax = self.maximum_value(temp.left);  
                #Compare variable maximum with leftMax and store greater value into maximum  
                maximum = max(maximum, leftMax);  
              
            #It will find largest element in right subtree  
            if(temp.right != None):  
                rightMax = self.maximum_value(temp.right);  
                #Compare variable maximum with rightMax and store greater value into maximum  
                maximum = max(maximum, rightMax);  
              
            return maximum; 

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
print(tree.maximum_value(tree.root))