class  PseudoQueue:
    def __init__(self):
        self.s1=[]
        self.s2=[]


    def enqueue(self,value):

        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(value)

        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()

    def peak(self):
        return self.s1[-1]


    def empty(self):
        return self.s1
