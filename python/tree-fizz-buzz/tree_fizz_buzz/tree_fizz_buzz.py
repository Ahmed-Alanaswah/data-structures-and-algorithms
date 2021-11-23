class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.center = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
    
        if traversal_type == "levelorder":
            return self.tree_breadth_first(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False


    def tree_breadth_first(self, start):
        if start is None:
            return 

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.center:
                queue.enqueue(node.center)
                
            if node.right:
                queue.enqueue(node.right)

        return traversal




tree = BinaryTree(3)
tree.root.left = Node(5)
tree.root.center = Node(15)
tree.root.right = Node(13)
tree.root.left.left = Node(20)
tree.root.left.center= Node(17)
tree.root.left.right = Node(16)

# print(tree.print_tree("levelorder"))

def tree_fizz_buzz(tree):
    newArr = []
    number = (" ".join(tree.split("-"))).split(" ")

    for i in  range(len(number)-1) :
        
        if int(number[i])%5==0 and int(number[i])%3==0:
            newArr.append("FizzBuzz")
                 
        elif int(number[i])%3==0:
            newArr.append("Fizz")
     
        elif int(number[i])%5==0:
            newArr.append("Buzz")
          
        else:
            newArr.append((number[i]))
          
    return newArr


print(tree_fizz_buzz(tree.print_tree("levelorder")))