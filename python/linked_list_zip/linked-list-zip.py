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

    def ziplist(self,list1,list2):
        # dummy = Node(0)
        # tail=dummy

        # while list1 and list2 :
        #     if list1.value < list2.value:
        #         tail.next = list1
        #         list1 =list1.next
        #     else:
        #         tail.next = list2
        #         list2 = list2.next
        #     tail = tail.next
        #     if list1:
        #         tail.next=list1
        #     elif list2:
        #          tail.next=list2
        # return dummy.next
  
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
     
         
    def tostr(self):
        output = "head -> "

        if self.head is None:
            output += "None"
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

ll2=LinkedList()
ll2.append(5)
ll2.append(6)
ll2.append(7)
ll2.append(8)

if __name__== "__main__":
    print(ll.tostr())
    print("====================")
    print(ll2.tostr())
    print("====================")
    ll.ziplist(ll,ll2)
    print(ll.tostr())
   
          
