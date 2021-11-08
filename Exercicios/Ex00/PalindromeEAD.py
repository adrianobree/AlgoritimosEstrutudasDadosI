

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()
palavra = input()
palavra = palavra.replace(" ", "")


for character in palavra:
    s.push(character)

reversed_palavra = ''
while not s.is_empty():
    reversed_palavra = reversed_palavra + s.pop()

if palavra == reversed_palavra:
    print('sim')
else:
    print('nao')