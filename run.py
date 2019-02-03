# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import pyrebase 

config = {
    "apiKey" : "AIzaSyBOzK-hHU8tIE6YbOG3NzbJSCiGspdC96c",
    "authDomain": "salad-34ad3.firebaseapp.com",
    "databaseURL": "https://salad-34ad3.firebaseio.com",
    "projectId": "salad-34ad3",
    "storageBucket": "salad-34ad3.appspot.com",
    "messagingSenderId": "102368296237"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

app = Flask(__name__)

commands = {"set username": "set username", "set phonenumber": "set phonenumber", "set location": "set location"}

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    number = request.values.get('from', None)
    print("response was: ", body)
    print("\nresponse was from: ", number)
    if body in commands:
        return process(commands[body])
    else:
    # Add a message
         resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)


def process(command):     #this function takes in valid commands and does to the correct action
    resp = MessagingResponse()
    if command == "set username":
        db.child("names").push({"name":"ashmita this worked"})
        resp.message("username added successfully")
    else:
        resp.message("no action required for command(valid)")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
