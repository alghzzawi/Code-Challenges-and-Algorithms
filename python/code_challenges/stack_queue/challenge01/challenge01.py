# Write here the code challenge solution

from inspect import stack


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
    
    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            temp.next = None
            return temp.value
        else:
            return("This stack is empty")

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")
    
    def empty(self):
        return self.size == 0

class MyQueue():
    def __init__(self):
        self.call_once=0

        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self,value):
        self.stack1.push(value)

    def push_stack2(self):

        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop()) 
    
    def pop(self):

        self.push_stack2()

        if self.call_once == 0:
            self.push_stack2()
        return self.stack2.pop()

    def peek(self):
        if self.call_once == 0:
            self.push_stack2()
        return self.stack2.peek()

    def empty(self):
        if self.call_once == 0:
            self.push_stack2()
        return self.stack2.empty()

if __name__ == "__main__":
    
    myqueue = MyQueue()

    myqueue.push(1)
    myqueue.push(2)

    print(myqueue.peek())
    print(myqueue.pop())
    print(myqueue.empty())