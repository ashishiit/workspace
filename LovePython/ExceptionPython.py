'''
Created on Oct 20, 2016

@author: S528358
'''
result = True
a = int(input('enter numerator'))
while result:
    try:
        b = int(input('enter denominator'))
        if b == 0:
            raise Exception('denominator can not be zero. please Enter again')
    except Exception as e:
        print(e)
    else:
        ans = a // b
        print('result = %d'%ans)
        result = False