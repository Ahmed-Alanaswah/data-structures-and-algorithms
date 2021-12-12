class Node:
    def __init__(self,value):
        self.value=value
        self.next= None
class LinkedList:
    def __init__(self):
        self.head= None

    def append(self,value):
        node= Node(value)
        if self.head is None:

            self.head=node

        else:
            current= self.head
            while current.next != None:
                current = current.next

            current.next = node

    def insert(self,value):
        node= Node(value)
        
        if self.head is None:
            self.head=node
        else:
            newNode= node
            newNode.next = self.head
            self.head= newNode
    def __str__(self):
        output = "head -> "

        if self.head is None:
            output += None
        else:
            current = self.head

            while(current) :
                output += f"{current.value} -> " 
                current= current.next   
            output += "None"
            return output
                