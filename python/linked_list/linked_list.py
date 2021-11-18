import re


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
        
    def ziplist(self,list1,list2):
     
        current1 = list1.head
        current2 = list2.head
        if list1 is None:
            return list2
        if list2 is None:
            return list1 
        while current1 != None and current2 != None:
            first_curr= current1.next
            sconed_curr= current2.next
            current1.next = current2
            current2.next = first_curr
            current1 = first_curr
            current2 = sconed_curr
 
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev 

    def palindrome(ll1):
        ll2 =ll1.reverse()
        if ll2 == ll1 :
            return True
        else :
            return False

        
        
            

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
ll.append(5)
ll.append(5)


ll.insert(0)
ll.insert("a")

ll2=LinkedList()
ll2.append(5)
ll2.append(6)
ll2.append(7)
ll2.append(8)
ll2.append(9)


if __name__== "__main__":
    print(ll)
    print("===================")
    print(ll2)
    # print("====================")
    # ll.ziplist(ll,ll2)
    # print(ll.__str__())
    print("===================")
    ll.reverse()
    print(ll.__str__())
    print("===================")
    ll.palindrome(ll)
    print(ll.__str__())