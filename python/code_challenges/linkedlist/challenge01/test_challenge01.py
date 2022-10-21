# Write your test here
import pytest
from challenge01 import LinkedList, Node


def test_nodes():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)

    node2 = Node(2)
    linkedList1.append(node2)

    node3 = Node(3)
    linkedList1.append(node3)

    node4 = Node(4)
    linkedList1.append(node4)

    actual = linkedList1.nodes
    expected = [1,2,3,4]
    assert actual == expected

def test_delete_tail():
    linkedList1 = LinkedList()
    node1 = Node(10)
    linkedList1.append(node1)

    node2 = Node(100)
    linkedList1.append(node2)

    node3 = Node(17)
    linkedList1.append(node3)

    node4 = Node(25)
    linkedList1.append(node4)

    linkedList1.delete(25)

    actual = linkedList1.nodes
    expected = [10,100,17]
    assert actual == expected
    





#=========================
#        fixture
#=========================

