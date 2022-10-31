# Write your test here
import pytest
from challenge02 import Stack,check_symbol


@pytest.mark.skip("todo")
def test_open_close_bracket_stack():

    stack1 = Stack()

    stack1.push(')')
    stack1.push('(')

    actual = check_symbol(stack1)
    expected = True, '()'
    assert actual == expected



@pytest.mark.skip("todo")
def test_open_close_all_bracket_stack():

    stack1 = Stack()

    stack1.push(')')
    stack1.push('(')
    stack1.push(']')
    stack1.push('[')
    stack1.push('}')
    stack1.push('{')

    actual = check_symbol(stack1)
    expected = True, '{}[]()'
    assert actual == expected


@pytest.mark.skip("todo")
def test_open_without_close_all_bracket_stack():
    stack1 = Stack()
    
    stack1.push(']')
    stack1.push('}')
    stack1.push('{')
    stack1.push('(')
    stack1.push('[')

    actual = check_symbol(stack1)
    expected = False
    assert actual == expected


@pytest.mark.skip("todo")
def test_open_close_all_bracket_stack_add_word():

    stack1 = Stack()

    stack1.push(']')
    stack1.push(')')
    stack1.push('(')
    stack1.push(')')
    stack1.push('hello')
    stack1.push('(')
    stack1.push('[')

    actual = check_symbol(stack1)
    expected = True, '[(hello)()]'
    assert actual == expected


@pytest.mark.skip("todo")
def test_open_and_close_all_bracket_stack():
    stack1 = Stack()

    stack1.push(']')
    stack1.push('}')
    stack1.push(')')
    stack1.push('(')
    stack1.push('{')
    stack1.push('[')

    actual = check_symbol(stack1)
    expected = True, '[{()}]'
    assert actual == expected