
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '***************'
auth_token = '****************'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+15017122661',
                              to='+15558675310'
                          )

print(message.sid)
