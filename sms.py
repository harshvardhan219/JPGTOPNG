from twilio.rest import Client 
 
account_sid = 'ACbdcf5384cbdacbc64d34fd261d41de4b' 
auth_token = 'use you auth_token' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12562428882',  
                              body='Send from SMS.py',      
                              to='+918700809998' 
                          ) 
 
print(message.sid)