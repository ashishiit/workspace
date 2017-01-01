'''
Created on Oct 28, 2016

@author: s528358
'''
def BaseConversion(decimal,base):
    conversion = '0123456789ABCDEF'
    if decimal < base:
        return conversion[decimal]
    else:
        s = BaseConversion(decimal//base, base) + conversion[decimal%base]
    return s
#print(2,2)


#write another function to do it iteratively
def BaseConversion2(decimal, base):
    conversion = '0123456789ABCDEF'
    a = []
    while decimal != 0:
        a.append(conversion[decimal%base])
#         print(a)
        decimal = decimal // base
    a.reverse()
#     for i in sort:
    return ''.join(a)
# print(BaseConversion(10, 2))
print(BaseConversion2(10, 2))   