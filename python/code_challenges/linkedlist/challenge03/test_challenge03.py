# Write your test here
import pytest
from challenge03 import LinkedList, Node

def test_node_delete_nth_node_from_end():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)

    node2 = Node(2)
    linkedList1.append(node2)

    node3 = Node(3)
    linkedList1.append(node3)

    node4 = Node(4)
    linkedList1.append(node4)

    node5 = Node(5)
    linkedList1.append(node5)

    linkedList1.remove_nth_end(2)

    actual = linkedList1.nodes
    expected = [1, 2, 3, 5]
    assert actual == expected


def test_head_node():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)

    linkedList1.remove_nth_end(1)

    actual = linkedList1.nodes
    expected = []
    assert actual == expected


def test_last_node():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)

    node2 = Node(2)
    linkedList1.append(node2)

    linkedList1.remove_nth_end(1)

    actual = linkedList1.nodes
    expected = [1]
    assert actual == expected