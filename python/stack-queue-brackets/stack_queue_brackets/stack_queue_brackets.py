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


def is_match(p1,p2):
    if p1 =="(" and p2==")":
        return True
    elif p1 =="{" and p2=="}":
        return True
    elif p1 =="[" and p2=="]":
        return True
    else: 
        return False
def is_paren_balance(paren_string):
    s=Stack()
    is_balance = True
    index=0
    paren_stringNew=""
    for i in paren_string:
        if i in "[(\{\})]":
           paren_stringNew += i
          

   
    while index < len (paren_stringNew) and is_balance:
        paren = paren_stringNew[index]
        if paren in "({[":
            s.push(paren)

        else: 
            if s.is_empty():
                is_balance = False    
            else :
                top= s.pop()

                if not is_match(top,paren):
                    is_balance = False
        index += 1
    if s.is_empty() and is_balance :
        return True
    else:
        return False   


print(is_paren_balance("([sssdgfg}gfgsssss])"))