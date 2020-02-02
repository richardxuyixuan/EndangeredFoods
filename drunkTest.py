from twilio.rest import Client
import requests

account_sid = 'AC5ee0218054a6d060e8ca36e49450850b'
auth_token = 'fdd1b53423469cb4d199ab2487e17cba'
client = Client(account_sid, auth_token)
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_iss = people['number']
#formulate the message that will be sent

def failMessage(clientName, contactNumber):
    Message = str(clientName) + ' failed Soberfy\'s sobriety test. Call ' + str(clientName) + ' immediately.'
    message = client.messages.create(
    to="+1" + contactNumber,
    from_="+12564748645",
    body=Message)
    message.sid

def passMessage(clientName, contactNumber):
    Message = str(clientName) + ' passed Soberfy\'s sobriety test, and is on their way home!'
    message = client.messages.create(
    to="+1" + contactNumber,
    from_="+12564748645",
    body=Message)
    message.sid

