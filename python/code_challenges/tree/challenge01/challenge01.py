# Write here the code challenge solution

class Node:
    '''this function to create node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right= None
class Tree:
    '''this function to create tree'''
    def __init__(self):
        self.root = None

binary_tree_array=[]
def pre_order(root):
    '''this function append the tree value in pre order way in binary_tree_array'''
    if root is not None:
        binary_tree_array.append(root.value)
    if root.left is not None:
        pre_order(root.left)
    if root.right is not None:
        pre_order(root.right)
    return binary_tree_array

def array_to_tree(root,pre_order,in_order):
    '''
    this fuction takes two array then add the value to the tree
    to create tree
    '''
    if len(pre_order)==0 or  len(in_order)==0:
        return

    node = Node(pre_order[0])
    root = node
    root_index_in_order = in_order.index(node.value)
    node.left = array_to_tree(root.left,pre_order[1:root_index_in_order+1], in_order[:root_index_in_order])
    node.right = array_to_tree(root.right,pre_order[root_index_in_order + 1:], in_order[root_index_in_order+1:])
    return root
