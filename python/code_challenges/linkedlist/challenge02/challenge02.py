# Write here the code challenge solution

class Node:
    instance_caunt=0
    def __init__(self,value):
        self.value = value
        self.next = None
        Node.instance_caunt+=1

class LinkedList:
    
    def __init__(self):
        self.head = None
        Node.instance_caunt=0

    def append (self, node):
        
        if self.head is None:
            self.head = node  

        elif node.value not in range(1,101):
            raise Exception (f'you gave the number {node.value}, The number of the value range [1, 100].')

        elif Node.instance_caunt > 100:
            raise Exception('The number of nodes in the list is in the range [1, 100].')
        
        else:
            current = self.head
            while  current.next is not None:
                current = current.next
            if current.value is node.value:
                raise Exception(f"this node {node.value} is already exist")

            current.next = node

    def middle_node(self):

        current = self.head
        count = 0
        mid_node=int(Node.instance_caunt/2)
        if self.head is None:
            raise Exception("The linked list is empty")
        
        while mid_node != count:
            current = current.next
            count+=1

        return current.value
        
    def printAll(self):

        if self.head is None:
            raise Exception("The linked list is empty")

        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next

if __name__ == '__main__':

    linkedList1 = LinkedList()

    node1 = Node(5)
    linkedList1.append(node1)

    node2 = Node(8)
    linkedList1.append(node2)

    node4 = Node(4)
    linkedList1.append(node4)

    node4 = Node(1)
    linkedList1.append(node4)

    node1 = Node(7)
    linkedList1.append(node1)
    # linkedList1.printAll()
    
    print(linkedList1.middle_node())
    
