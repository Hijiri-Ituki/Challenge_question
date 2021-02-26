class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):                                
        return len(self.items)

correct = [1,2,3,4,5]
reverse = []

stack = Stack()
for i in correct:
    stack.push(i)

while stack.size():
    reverse.append(stack.pop())    #ここのコードのみ解答閲覧

print(reverse)
