from stack_queue_brackets import __version__
from stack_queue_brackets.stack_queue_brackets import *

def test_version():
    assert __version__ == '0.1.0'


def test_isbalance_bracket_isFlse():

    actual = is_paren_balance("([sssdgfg}gfgsssss])")
    excpected = False
    assert excpected == actual

def test_isbalance_bracket_isTrue():

    actual = is_paren_balance("([sssdgfggfgsssss])")
    excpected = True
    assert excpected == actual