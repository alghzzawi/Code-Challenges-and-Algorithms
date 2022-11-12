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
        self.pre_order_array=[]

    def pre_order(self, root):
        if root is not None:
            self.pre_order_array.append(root.value)
        if root.left is not None:
            self.pre_order(root.left)
        if root.right is not None:
            self.pre_order(root.right)

    def array_To_bst(self,arr=[]):
        '''this function create tree of node from array of integer'''
        if not arr :
            return None
        arr.sort()
        mid = len(arr)//2
        root = Node(arr[mid])
        root.left = self.array_To_bst(arr[:mid])
        root.right = self.array_To_bst(arr[mid+1:])
    
        return root


if __name__=='__main__':
    tree=Tree()
    array=[1,3]
    root = tree.array_To_bst(array)
    tree.pre_order(root)  # root - left - right
    print(tree.pre_order_array)
