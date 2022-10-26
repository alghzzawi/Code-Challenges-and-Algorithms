# Write here the code challenge solution

import numbers


class Node:
    instance_caunt=0
    def __init__(self,value):
        self.value = value
        self.next = None
        Node.instance_caunt+=1

class LinkedList:
    Node.instance_caunt=0
    def __init__(self):
        self.head = None
        self.nodes=[]
    def append (self, node):
        
        if self.head is None:
            self.head = node  

        elif node.value not in range(0,101):
            raise Exception (f'you gave the number {node.value}, The number of the value range [1, 100].')

        elif Node.instance_caunt > 100 and Node.instance_caunt < 0 :
            raise Exception('The number of nodes in the list is in the range [1, 100].')
        
        else:
            current = self.head
            while  current.next is not None:
                current = current.next
            if current.value is node.value:
                raise Exception(f"this node {node.value} is already exist")

            current.next = node
        self.nodes.append(node.value)
        
    def delete (self, node):
        self.nodes.remove(node)
        if self.head is None:
            return
        elif self.head.value is node:
            self.head = self.head.next
            return

        current = self.head
        while current.next.value is not node:
            current = current.next

        delete_node = current.next
        current.next = delete_node.next
    
    def printAll(self):

        if self.head is None:
            raise Exception("The linked list is empty")

        else:
            current = self.head
            while current is not None:
                print(current.value, end=' -> ')
                current = current.next

    def remove_nth_end (self, nth_node):
        current = self.head
        number_node = 0
        
        while current is not None:
            current = current.next
            number_node+=1
        if nth_node > number_node:
            raise Exception('1 <= nth <= number of nodes')



        number_node-=nth_node
        current = self.head
        for i in range(number_node):
            current = current.next
        # print(current.value)
        self.delete(current.value)

if __name__ == '__main__':

    linkedList1 = LinkedList()
    node1 = Node(5)
    linkedList1.append(node1)

    node2 = Node(8)
    linkedList1.append(node2)

    node3 = Node(10)
    linkedList1.append(node3)

    node4 = Node(4)
    linkedList1.append(node4)

    linkedList1.remove_nth_end(1)
    # linkedList1.printAll()
    print(linkedList1.nodes)