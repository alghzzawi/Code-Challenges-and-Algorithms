# Write your test here
import pytest
from challenge01 import MyQueue

def test_peek_queue(nirvana_nodes):

    actual = nirvana_nodes.peek()
    expected = 1
    assert actual == expected

def test_pop_queue(nirvana_nodes):

    actual = nirvana_nodes.pop()
    expected = 1
    assert actual == expected

def test_empty_queue(nirvana_nodes):

    actual = nirvana_nodes.empty()
    expected = False
    assert actual == expected


#######################
# Fixtures
#######################


@pytest.fixture
def nirvana_nodes():
    myqueue = MyQueue()

    myqueue.push(1)
    myqueue.push(2)
    return myqueue