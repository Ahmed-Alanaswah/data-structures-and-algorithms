
from stack_and_queue.stack import EmtyStack, Stack

import pytest
def test_push(stack):
    actual=stack.top.value
    expected="34"
    assert expected == actual

def test_pop(stack):
    actual=stack.pop()
    expected="34"
    assert expected == actual
def test_peek(stack):
    actual=stack.top.value
    expected="34"
    assert expected == actual
def test_empty_pop(stack):
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    actual=stack.top
    expected=None
    assert expected == actual

def test_estantiate_empty_stack():
    stack=Stack()
    actual=stack.top
    expected=None
    assert expected == actual


@pytest.fixture

def stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push("python")
    stack.push("34")



    return stack