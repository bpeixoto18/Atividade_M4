from twilio.rest import TwilioRestClient



accountSID = 'ACxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+15558675309'
twilioNumber = '+15558675309'



def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)