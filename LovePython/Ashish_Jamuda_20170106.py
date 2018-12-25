'''
Created on Jan 6, 2017

@author: S528358
'''

def Fact(N):
    if N == 0:
        return 1
    else:
        ans = N * Fact(N-1)
    return ans
def fBirthdayProb(N):
    '''Fact() function to calculate factorial'''
    temp = Fact(365)/Fact(365-N)
    temp = temp/pow(365,N)
    return 1-temp

    



    