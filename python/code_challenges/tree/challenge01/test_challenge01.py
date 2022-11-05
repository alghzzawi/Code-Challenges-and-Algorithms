# Write your test here
import pytest 
from challenge01 import Tree, array_to_tree,pre_order

# @pytest.mark.skip("todo")
def test_binary_tree():
    pre_order_array = [3,9,20,15,7]
    in_order_array = [9,3,15,20,7]

    tree = Tree()
    root_node = array_to_tree(tree.root,pre_order_array, in_order_array)
    
    expected=pre_order(root_node)
    actual=[3, 9, 20, 15, 7]
    assert actual==expected

@pytest.mark.skip("todo")
def test_binary_order_tree_one_node():
    pre_order_array = [-1]
    in_order_array = [-1]

    tree = Tree()
    root_node = array_to_tree(tree.root,pre_order_array, in_order_array)
    
    expected=pre_order(root_node)
    actual=[-1]
    assert actual==expected

@pytest.mark.skip("todo")
def test_binary_pre_order_tree():
    pre_order_array = [3,9,1,2,20,15,7]
    in_order_array = [1,9,2,3,15,20,7]

    tree = Tree()
    root_node = array_to_tree(tree.root,pre_order_array, in_order_array)
    
    expected=pre_order(root_node)
    actual=[3, 9, 1, 2, 20, 15, 7]
    assert actual==expected
