'''
Created on Jan 1, 2017

@author: S528358
'''
from twilio.rest import TwilioRestClient
ACCOUNT_SID = "AC901124ef5a6aa51ab36bf783d67f2683"
AUTH_TOKEN = "89fa78d7dfa31a343339db6887d11436"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# message = client.messages.create(
#     body="Hello Monkey!",  # Message body, if any
#     to="+12125551234",
#     from_="+15105551234",
# )
# print (message.sid)
a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
l = [1] * len(a)
l[0] = 1
for i in range(1,len(a)):
    test = []
    for j in range(0,i):
        message = client.messages.create(
        body="Hello World %d"%j,  # Message body, if any
        to="+18166151879",
        from_="+19788775036",
)
#         print('value of i%d and j%d'%(i,j))
        if a[i] > a[j]:
            test.append(l[j])
    if test == []:
        continue
    else:
        l[i] = 1 + max(test)
#     print('%d and %d'%(i, l[i]))
# print(l, end = ' ')
print('length of longest subsequence = %d'%max(l))