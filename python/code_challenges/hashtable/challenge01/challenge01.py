# Write here the code challenge solution



class Node:
    def __init__(self, value) -> None:
        """this function create a Node"""
        self.value = value
        self.left = None
        self.right = None



class Tree:
    def  __init__(self):
        self.root=None
    def insert(self,value):
        """add node to BST"""
        if value == None:
            return

        node= Node(value)
        if self.root==None:
            self.root=node
            return self.root
        
        current=self.root
        while True:
            if current.value>node.value:
                if current.left==None:
                    current.left=node
                    return self.root
                current=current.left
            else:
                if current.right==None:
                    current.right=node
                    return self.root
                current=current.right

    def pre_order(self, root):
        if root is not None:
            print(root.value)
        if root.left is not None:
            self.pre_order(root.left)
        if root.right is not None:
            self.pre_order(root.right)

def findSummation (root, k):
    """find if in BST there tow element summation is equal k"""
    if root is None:
        return
    arr = []
    def inorder(root):
        if root:
            inorder(root.left)
            arr.append(root.value)
            inorder(root.right)            
    inorder(root)
    first = 0
    last = len(arr) - 1
    while first < last:
        sum = arr[first] + arr[last]
        if sum == k:
            return True
        elif sum < k:
            first += 1
        else:
            last -= 1
    return False
