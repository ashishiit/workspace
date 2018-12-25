'''
Created on Sep 15, 2018

@author: S528358
'''
def Puzzle(num):
    count = 0
    num_str = str(num)
    
    for i in num_str:
        
        if int(i)==1 or int(i)==2 or int(i)==3 or int(i)==5 or int(i)==7:
            count = count + 0
        elif int(i)==0 or int(i)==4 or int(i)==6 or int(i)==9:
            count = count + 1
        elif int(i)==8:
            count = count + 2
    return count

print(Puzzle(1288))