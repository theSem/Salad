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

db.child("names").push({"name":"lukas"})

app = Flask(__name__)

messages = {"foo": "bar", "dummy": "data", "crawl": "walk"}

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    print("response was: ", body)
    if body in messages:
        resp.message(messages[body])
    else:
    # Add a message
         resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
