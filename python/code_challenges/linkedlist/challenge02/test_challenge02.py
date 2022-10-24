# Write your test here
import pytest
from challenge02 import Node,LinkedList

def test_find_middle_node_odd():
    linkedList1 = LinkedList()

    node1 = Node(1)
    linkedList1.append(node1)

    node2 = Node(2)
    linkedList1.append(node2)

    node4 = Node(3)
    linkedList1.append(node4)

    node4 = Node(4)
    linkedList1.append(node4)

    node1 = Node(5)
    linkedList1.append(node1)
    
    actual = linkedList1.middle_node()
    expected = 3
    assert actual == expected


def test_find_middle_node_even():
    linkedList2 = LinkedList()

    node_1 = Node(1)
    linkedList2.append(node_1)

    node_2 = Node(2)
    linkedList2.append(node_2)

    node_3 = Node(3)
    linkedList2.append(node_3)

    node_4 = Node(4)
    linkedList2.append(node_4)

    node_5 = Node(5)
    linkedList2.append(node_5)

    node_6 = Node(6)
    linkedList2.append(node_6)
    
    actual = linkedList2.middle_node()
    expected = 4
    assert actual == expected