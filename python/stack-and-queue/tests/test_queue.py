from stack_and_queue.queue import Queue


def test_is_empty():
    queue= Queue()
    expected = True
    actual = queue.is_empty()

    assert expected == actual


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("python")

    expected ="python"
    actual = queue.rear.value

    assert expected==actual


def test_dequeue():
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue("python")
   
   

    expected =1
    actual =  queue.dequeue()

    assert expected==actual


def test_peek():
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue("python")
   
    peek=queue.rear.value 

    expected ="python"
    actual =   peek

    assert expected==actual




def test_empty_AfterMultyDeque():
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue("python")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    empty =queue.front
   

    expected =None
    actual =  empty

    assert expected==actual


def test_istantiate_empty_queue():
    queue = Queue()
    

    empty =queue.front
   

    expected =None
    actual =  empty

    assert expected==actual


# def test_call_empty_queue():
#     queue = Queue()
    

#     empty =queue.dequeue()
   

#     expected =empty
#     actual =  empty

#     assert expected==actual