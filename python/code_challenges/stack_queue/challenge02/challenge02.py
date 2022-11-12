# Write here the code challenge solution

class Node:
    def __init__(self, value):
        '''this constractor create node'''
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        '''this constractor create stack'''
        self.top = None
        self.size = 0
        self.open_bracket={")" : "(", "]" : "[", "}" : "{"}

    
    def push(self, symbol):
        '''this function create new node and push it to stack'''
        node = Node(symbol)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
    
    def pop(self):
        '''this function pop/remove the last node that pushed in stack '''
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            temp.next = None
            return temp.value
        else:
            return("This stack is empty")

    def empty(self):
        '''this function check if stack is empty or not empty'''
        return self.size == 0

    def peek(self):
        '''this function return the last value in stack'''
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")
    

def check_symbol(stack):
    '''this function check if each open bracket have close bracket with same type'''
    stack_open_bracket=[]
    all_bracket=''
    while not stack.empty():

        if stack.peek() in stack.open_bracket.values():
            stack_open_bracket.append(stack.peek())
        
        elif stack.peek() in stack.open_bracket.keys():
            if stack_open_bracket == [] or stack_open_bracket.pop() != stack.open_bracket[stack.peek()]:
                return False
        else:
            pass

        all_bracket+=stack.peek()
        stack.pop()
    print(stack_open_bracket)
    return stack_open_bracket == [],all_bracket
        




if __name__ == '__main__':
    stack1 = Stack()
    
    stack1.push(']')
    stack1.push('}')
    stack1.push(')')
    stack1.push('(')
    stack1.push('{')
    stack1.push('[')





    print(check_symbol(stack1))
    # print(stack1.pop())


