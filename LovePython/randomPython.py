'''
Created on Sep 16, 2016

@author: S528358
'''
#print('hello Python')
result = True
while result:
    try:
        a = int(input("enter any integer"))
    except Exception as e:
        print('not an integer',str(e))
    else:
        print('you entered a valid integer = %d'%a)
        result = False
            
