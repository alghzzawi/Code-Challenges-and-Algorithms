# Write here the code challenge solution

from logging import exception


class Node:
    instance_caunt=0
    def __init__(self,value):
        self.value = value
        self.next = None
        Node.instance_caunt+=1

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.nodes=[]

    def append (self, node):
        
        if node.value not in range(-1000,1001):
            print (f'you gave the number {node.value}, The number of the value range [-1000, 1000].')
            return
        
        elif self.head is None:
            self.head = node
            self.nodes.append(node.value)
        
        elif self.head.value is node.value:
            raise Exception(f"this node {node.value} is already exist")
            

        else:
            current = self.head
            # print (current.value)
            while  current.next is not None:
                current = current.next
            if current.value is node.value:
                raise Exception(f"this node {node.value} is already exist")

            current.next = node
            self.nodes.append(node.value)
        
    def delete (self, node):
        

        if node.next is None:
            return

        else:
            self.nodes.remove(node.value)
            next_node = node.next

            node.value = next_node.value

            node.next = next_node.next

            next_node.next = None
            

    def printAll(self):

        if self.head is None:
            raise Exception("The linked list is empty")

        elif Node.instance_caunt not in range(2,1000):
            raise Exception('The number of the nodes in the given list is in the range [2, 1000].')
        
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next



if __name__ == "__main__":

    linkedList1 = LinkedList()
    node1 = Node(5)
    linkedList1.append(node1)

    node2 = Node(8)
    linkedList1.append(node2)

    node3 = Node(10)
    linkedList1.append(node3)

    node4 = Node(4)
    linkedList1.append(node4)

    linkedList1.delete(node1)
    linkedList1.printAll()

    print(linkedList1.nodes)
