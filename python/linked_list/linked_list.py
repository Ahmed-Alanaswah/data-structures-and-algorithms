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
            head=node
        else:
            current= self.head
            while current.next != None:
                current = current.next
            current.next = node  
    def __str__(self):
        output="head -> "
        if self.head is None:
            output += None
        else:
            current = self.head
            while (current) :
                output += f"{current.value} -> "    
            output += "None"
            return output
ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print(ll)
if __name__== "__main__":
    pass