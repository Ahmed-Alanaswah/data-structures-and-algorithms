class Node:

    def __init__(self,value) :
        self.value  = value
        self.next = None

    

class EmtyQueue(Exception):
    pass
class Queue:
    """
    class that implement the queue data structure
    """
    def __init__(self):
        self.front=None
        self.rear=None


    def enqueue(self,value):
        node= Node(value)

        if not self.rear :
            self.rear = node 
            self.front = node
        else:
           self.rear.next = node
           self.rear = node

    def dequeue(self):
        if self.front is None:
            raise EmtyQueue("this is queue is empty")
        temp = self.front
        self.front = self.front.next
        temp.next= None
        return temp.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
           raise EmtyQueue("this is queue is empty") 


    def is_empty(self):
       return self.front == None

    def printdata(self):
        if self.front== None:
           print("the queue is empty")
        else:
            print("queue data:")
            print("front ====>",self.rear.value ,'<=====')

class AnimalShelter:

    def __init__(self):

        self.dog=Queue()
        self.cat=Queue()

    def enqueue(self, animal):

        if animal.type =='cat':
            self.cat.enqueue(animal.nick_name)
            return animal
        elif animal.type =='dog':
            self.dog.enqueue(animal.nick_name)
            return animal
        else:

            return 'This is not cat or dog'

    def dequeue(self, pref):

        if pref == 'cat':

            if self.cat.is_empty():
                raise Exception("empty")
            else:
                return self.cat.dequeue()

        elif pref == 'dog':

            if self.dog.is_empty():
                raise Exception("empty")
            else:
                return self.dog.dequeue()

        else:

            return None

class Cat:

    def __init__(self,nick_name):
        self.nick_name=nick_name
        self.type='cat'

class Dog:

    def __init__(self,nick_name):
        self.nick_name= nick_name
        self.type='dog'



if __name__ == '__main__':

    animalShelter = AnimalShelter()
    dog_one = Dog("Myu")
    dog_two = Dog("Muuu")
    cat_one =Cat("muhhhhhhhuu")
    cat_two =Cat("muudddu")
    dog_three = Dog("KuuuuE")
    animalShelter.enqueue(dog_one)
    animalShelter.enqueue(dog_two)
    animalShelter.enqueue(dog_three)
    animalShelter.enqueue(cat_one)
    animalShelter.enqueue(cat_two)
    animalShelter.dequeue(cat_one)
    animalShelter.cat.printdata()