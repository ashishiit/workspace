'''
@author: s528358
'''
def Data_Munging_Kata(N):    
    min_precipitation = []
    with open("C:\\Users\\s528358\\eclipse-workspace\\Data_Munging_Kata\\weather.txt") as f: #read input file
        next(f) #skip the first line of input file
        for line in f:
            min_precipitation.append(int(line.split()[4]))
    min_precipitation = min(min_precipitation) # get minimum precipitation   
    with open("C:\\Users\\s528358\\eclipse-workspace\\Data_Munging_Kata\\weather.txt") as f: #read input file
        next(f)
        DateDay = {1:'Wednesday', 2:'Thursday', 3:'Friday', 4:'Saturday', 5:'Sunday', 6:'Monday', 7:'Tuesday'} #dictionary to enumerate the date and corresponding days
        count = 0 # track number of "best day" vacation <= N
        for line in f:
            a = line.split()
            a[0] = int(a[0])
            a[2] = int(int(a[2])*1.8 + 32) # convert Celsius to Fahrenheit
            a[3] = int(int(a[3])*1.8 + 32) # convert Celsius to Fahrenheit
            a[4] = int(a[4])    
            if a[4] == min_precipitation and (a[3]>=70 and a[2]<=85): # check for minimum precipitation and lower temperature>=70F and higher temperature<=85
                if a[0]%7 in DateDay: # get the date and day
                    if count < N:
                        suffix = ''
                        ''' get relevant suffix for days
                        '''
                        if a[0]%10 == 1:
                            suffix = suffix + 'st'
                        elif a[0]%10 == 2:
                            suffix = suffix + 'nd'
                        elif a[0]%10 == 3:
                            suffix = suffix + 'rd'
                        else:
                            suffix = suffix + 'th'        
                        print(DateDay[a[0]%7]+' the ' + str(a[0]) +suffix +' day of the month is the best day for a picnic.')
                        count = count + 1
N = int(input('enter number of days = ')) #take input from user
Data_Munging_Kata(N)