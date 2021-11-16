from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter,Node,Queue,Cat,Dog

def test_version():
    assert __version__ == '0.1.0'


def test_enqueue():
    animalShelter = AnimalShelter()
    dog_one = Dog("Myu")
    dog_two = Dog("Muuu")
    # cat_one =Cat("muuu")
    dog_three = Dog("KuuuuE")
    animalShelter.enqueue(dog_one)
    animalShelter.enqueue(dog_two)
    animalShelter.enqueue(dog_three)
    
    actual = animalShelter.dog.rear.value

    excepted ="KuuuuE"
    # actual = animalShelter.enqueue(cat_one)
    assert excepted == actual


def test_dequeue():
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
    
    actual = animalShelter.cat.rear.value

    excepted ="muudddu"
    # actual = animalShelter.enqueue(cat_one)
    assert excepted == actual