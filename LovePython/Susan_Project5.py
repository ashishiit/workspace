fileInput = open('tickets5-project.txt','r+')
def getFirstName(ticketInfo):
    return ticketInfo.split(' ')[1]
def getLastName(ticketInfo):
    return ticketInfo.split(' ')[2]
def getRow(ticketInfo):
    return ticketInfo.split(' ')[3]
def getSeat(ticketInfo):
    return ticketInfo.split(' ')[4]
def toString(firstName, lastName, row, seat):
    print()
    print('Welcome to Bearcat Baseball, %s %s'%(firstName, lastName))
    print('Your row is %s'%row)
    print('Your seat number is %s'%seat)
def ticketReader(ticketNum, fileInput):
    fileInput = open('tickets5-project.txt','r+')
    count = 0
    for line in fileInput:
        if ticketNum == line.split(' ')[0]:
            count = count + 1
            ticketInfo = line
            firstName = getFirstName(ticketInfo)
            lastName = getLastName(ticketInfo)
            row = getRow(ticketInfo)
            seat = getSeat(ticketInfo)
            toString(firstName, lastName, row, seat)
    if count == 0:
        print('No ticket reservation')
        print()
ticketNum = input('Enter your ticket number (0 to stop scanning in):')
if ticketNum == '0':
    print('Have a nice day!')
else:
    while ticketNum != '0':        
        ticketReader(ticketNum, fileInput)
        ticketNum = input('Enter your ticket number (0 to stop scanning in):')
        if ticketNum == '0':
            print()
            print('Welcome to Bearcat Baseball, enjoy the game!')
            break