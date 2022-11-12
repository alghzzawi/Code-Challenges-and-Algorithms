# Write your test here
import pytest
from challenge03 import Tree


def test_array_To_bst_tree1(first_tree):
    actual = first_tree
    expected = [0, -3, -10, 9, 5]
    assert actual == expected

def test_array_To_bst_tree2(secand_tree):
    actual = secand_tree
    expected = [3,1]
    assert actual == expected


#=========================
#        fixture
#=========================

@pytest.fixture
def first_tree():
    tree1=Tree()
    list= [0,-3,-10,5,9]
    root=tree1.array_To_bst(list)
    tree1.pre_order(root)
    return tree1.pre_order_array

@pytest.fixture
def secand_tree():
    tree2=Tree()
    list= [3,1]
    root=tree2.array_To_bst(list)
    tree2.pre_order(root)
    return tree2.pre_order_array