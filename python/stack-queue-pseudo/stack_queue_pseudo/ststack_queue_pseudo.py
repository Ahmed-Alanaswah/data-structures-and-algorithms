# from inspect import stack
# from stack_and_queue.node import Node


class Node:

    def __init__(self,value) :
        self.value  = value
        self.next = None

    

class EmtyStack(Exception):
    pass
class Stack:
    """
    class that implement the stack data structure
    """
    def __init__(self) :
        self.top=None
        



    def push(self,value):
        node= Node(value)
        # if not self.top:
        if self.top:
            node.next=self.top
        self.top=node

    def pop(self):
        if self.top == None:
            raise EmtyStack("this stack is empty")
            
        temp =self.top
        self.top= temp.next
        temp.next =None
     
        return temp.value

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise EmtyStack("this stack is empty")


    def is_empty(self):
        return self.top ==None 

   
   


class  PseudoQueue:
    def __init__(self):
       
        self.s2=Stack()
        self.s1=Stack()


    def enqueue(self,value):
        
        return self.s1.push(value)
        # while self.s1:
        #     self.s2.push(self.s1.pop())
        # self.s1.push(value)

        # while self.s2:
        #     self.s1.push(self.s2.pop())
        # return self.s1.push(self.s2.pop())
    def dequeue(self):
        if  self.s2.is_empty():
            while not self.s1.is_empty() :
                self.s2.push(self.s1.pop())
        return self.s2.pop()
        
        # if  self.s1.is_empty():
        #     while self.s2:
        #         self.s1.push(self.s2.pop())
        #     # self.s1.pop()

    def peak(self):
        return self.s2.top.value


    def empty(self):
        return self.s2




queue= PseudoQueue()

# queue.enqueue(2)
# queue.enqueue(3)
# queue.dequeue()
# queue.print()