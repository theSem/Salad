from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACbe847de66cee93f12d7cae40fdfe9c1f'
auth_token = '48c93122fd255fe2c7aeb5a555a1956b'
client = Client(account_sid, auth_token)

def main():
    message = client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17045869102',
                     to='+16512530822'
                 )

    print(message.sid)

if __name__ == '__main__':
    main()
