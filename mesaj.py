# -*- coding: utf-8 -*-
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8f7f6a32379f1b451aae819e7228a6c8"
# Your Auth Token from twilio.com/console
auth_token  = "aa59d2e6f341b52cab7e3bc38a624577"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+905533155794",
    from_="+15005550006",
    body="Nenra Bishop Giris Kodu 1234")

print(message.sid)