from twilio.rest import Client

def sms(name,link,state,city):
    account_sid='SID given by Twilio'
    auth_token='Token given by Twilio'
    client=Client(account_sid,auth_token)

    call=client.calls.create(twiml='<Response><Say>I am'+ name+' I am in danger. I have mailed my location to you. Help me fast. </Say></Response>', to='Twilio verified phone number',from_='Number given by Twilio')

    message = client.messages.create(body='I am '+name+'. I am in danger. I have sent my location. Help me fast.  '+ link, to='Twilio verified phone number',from_='Number given by Twilio')
    print(call.sid)
    print(message.sid)

