# Write your test here
from challenge01  import *
import pytest


def test_1():
    tree=Tree()

    tree.insert(7)
    tree.insert(2)
    tree.insert(9)
    tree.insert(1)
    tree.insert(5)
    tree.insert(14)


    actual = findSummation(tree.root,3)
    expected = True
    assert actual == expected

def test_2():
    tree1=Tree()

    tree1.insert(7)
    tree1.insert(2)
    tree1.insert(9)
    tree1.insert(1)
    tree1.insert(5)
    tree1.insert(14)


    actual = findSummation(tree1.root,13)
    expected = False
    assert actual == expected

def test_3():
    tree2=Tree()

    tree2.insert(7)
    tree2.insert(2)
    tree2.insert(9)
    tree2.insert(1)
    tree2.insert(5)
    tree2.insert(14)


    actual = findSummation(tree2.root,4)
    expected = False
    assert actual == expected