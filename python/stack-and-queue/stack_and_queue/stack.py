from inspect import stack
from stack_and_queue.node import Node


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

   
   
