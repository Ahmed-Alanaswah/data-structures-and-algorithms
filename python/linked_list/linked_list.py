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
         
    def recInclude(self,node,key):
        if node == None:
            return False
        if node.value == key:
            return True 
        return self.recInclude(node.next,key)

    def include(self,key):
        current = self.head
        while current != None:
            if current.value == key:
                return True
           
            current = current.next 
        return False

    def addBefor(self,value,nextNode):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.value==nextNode:
            newNode= Node(value)
            newNode.next = self.head
            self.head= newNode
            return
        current = self.head
        while current.next is not None:
            if current.next.value == nextNode:
                break
            current=current.next
        if current is None:
            print("node is not found")
        else:
            newNode= Node(value)
            newNode.next = current.next
            current.next= newNode    
        

    def addAfter(self,value,prevNode):
        current = self.head
        while current is not None:
            if prevNode == current.value:
                break
            current= current.next
        if current is None:
            print("node is not present in ll")

        else:
            newNode = Node(value)
            newNode.next =current.next
            current.next = newNode


    def printNthFromLast(self, n):
        temp = self.head # used temp variable
          
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
          
        # print count 
        if n > length: # if entered location is greater 
                       # than length of linked list
            print('Location is greater than the' +
                         ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        return temp.value
        


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
            

ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)


ll.insert(0)
ll.insert("a")

if __name__== "__main__":
    print(ll)
    print(ll.printNthFromLast(1))
    # print(ll.include(0))
    # print(ll.addAfter(6,2))
    # print(ll.addBefor("b",4))
    # print(ll.addBefor("d","b"))
   
    
