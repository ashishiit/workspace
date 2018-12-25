'''
Created on Jun 7, 2017

@author: S528358
'''
class Stack:
    def __init__(self):
        self.a = []
    def Push(self, item):
        self.a.append(item)
    def Pop(self):
        return self.a.pop()
    def Peek(self):
        return self.a[len(self.a)-1]
    def Display(self):
        print(self.a)
    def IsEmpty(self):
        return self.a == []
s = Stack()
output = open("output.txt", "r+")
inp = open('IntroductionToSupply.txt', 'r+')
# print(len(inp))
for i in inp:
#     output.writelines(i)
    count = len(i)
    temp = i.split(' ')
temp = temp[::-1]
for word in temp:
    s.Push(word)
    s.Push(' ')
# s.Display()
first = []
# second = []
count = 0
line = 0
s.Pop()
while not s.IsEmpty():    
    count = count + len(s.Peek())
    if count <= 42:
        first.append(s.Pop())
    elif count > 42:
#         print(first)
        output.writelines(''.join(first))
        count = 0
        first = []
        line = line + 1
        if line == 1:
            output.writelines('\n')
        else:
            output.writelines('\n\n')
            if line == 2:
                line = 0        
output.writelines(''.join(first))