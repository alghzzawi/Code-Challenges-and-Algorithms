# Write here the code challenge solution

class Node:
    def __init__(self, val):
        self.value=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def add(self,val):
        node=Node(val)

        if not self.head:
            self.head = node
        
        else:
            current=self.head
            while current.next:
                current=current.next
            
            current.next = node
    
    def __str__(self):
        value=[]
        current=self.head
        while current:
            value.append(current.value)
            current=current.next
        return f'{value}'


class HashTabel:
    def __init__(self,size=5):
        self.size=size
        self.map=[None]*size # that will create array with this size contact None for each index
    
    def custom_hash(self,key):
        sum_of_asccii=0
        for char in key:
            asccii_of_char=ord(char)
            sum_of_asccii+=asccii_of_char
        temp=sum_of_asccii*19
        index=temp%self.size
        return index
    
    def find_repeated(self,words):
        words=words.split(' ')

        for word in words:
            hashed_key=self.custom_hash(word)
            if not self.map[hashed_key]:# if its empty
                self.map[hashed_key]=[word]
            else:
                
                if isinstance(self.map[hashed_key],LinkedList):
                    current=self.map[hashed_key].head
                    while current.next:
                        if current.value[0] == word:
                            return word
                        current=current.next
                    self.map[hashed_key].add([word])
                else: # if the key bucket contains one piar only
                    if self.map[hashed_key][0] == word:
                        return word
                    chain=LinkedList()
                    existing_pair=self.map[hashed_key]
                    new_pair=[word]
                    self.map[hashed_key]=chain
                    chain.add(existing_pair)
                    chain.add(new_pair)
        return 'No Repetition'
        


if __name__=="__main__":
    hashtabel1= HashTabel()
    print(hashtabel1.find_repeated('that a she want to go hello why no but Write function  will take string as parameter and return the first repeated word in that'))

