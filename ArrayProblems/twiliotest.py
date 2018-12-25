'''
Created on Dec 21, 2018

@author: S528358
'''
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC5603da05a252a593639359946bae5a49'
auth_token = '6e5ca3c110da8e04a8538fc16bd3bc6b'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+6602353180',
                     to='+6605280321'
                 )

print(message.sid)
# message = client.messages.create(
#                               from_='+6602353180',# twilio phone number
#                               body='test',
#                               to='+3122732470'
#                           )
# 
# print(message.sid)