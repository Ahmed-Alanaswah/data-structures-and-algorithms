from stack_queue_pseudo import __version__
from stack_queue_pseudo.ststack_queue_pseudo import PseudoQueue

def test_version():
    assert __version__ == '0.1.0'





def test_is_empty():
    queue= PseudoQueue()
    expected = []
    actual = queue.empty()

    assert expected == actual


def test_enqueue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("python")

    expected ="python"
    actual = queue.s1[0]

    assert expected==actual


def test_dequeue():
    queue = PseudoQueue()
    
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue("python")
   
   

    expected =1
    actual  = queue.s1[-1]

    assert expected==actual


def test_peek():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue("python")
   
    peek= queue.s1[0]

    expected ="python"
    actual =   peek

    assert expected==actual

