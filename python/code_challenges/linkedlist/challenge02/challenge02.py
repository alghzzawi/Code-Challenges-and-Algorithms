# Write here the code challenge solution

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
# []->[]->[]->[]->None
# ->  ->  ->  ->
# []->[]->[]->None
# ->  ->  ->  ->
        if self.head is None:
            return
        fast = self.head
        slow = self.head

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
        return slow.value
        
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
    
