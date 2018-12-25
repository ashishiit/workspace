'''
Created on Jul 16, 2018

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
inp = open('1.5 Results from the 3D Process.txt', 'r+',encoding='utf8', errors='ignore')
temp_s = []
for i in inp:
    print(str(i))
    temp_s = temp_s + str(i).split()

    count = len(i)

temp_s = temp_s[::-1]
for word in temp_s:
    s.Push(word)
    s.Push(' ')

first = []

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

print(temp_s)