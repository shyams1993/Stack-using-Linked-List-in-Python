class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Stack():
    def __init__(self):
        self.top = None #tail
        self.bottom = None #head
        self.length = 0
    
    def __str__(self):
        return str(self.__dict__)

    def printer(self):
        currentPtr = self.bottom
        box = []
        while currentPtr != None:
            box.append(currentPtr.data)
            currentPtr = currentPtr.next
        return box

    def push(self,data):
        newElement = Node(data)
        if self.bottom == None:
            self.bottom = newElement
            self.top = self.bottom
            self.length += 1
        else:
            self.top.next = newElement
            self.top = newElement
            self.length += 1

    def pop(self):
        currentPtr = self.bottom
        i=0
        while i<self.length:
            if i == self.length-2:
                currentPtr.next = None
                self.top = currentPtr
                self.length -= 1
            currentPtr = currentPtr.next
            i += 1
                
    def peek(self):
        return self.top.data

m = Stack()
m.push(10)
m.push(11)
m.push(12)
m.push(13)
m.push(14)
m.pop()
print(m)
print(m.peek())
print(m.printer())