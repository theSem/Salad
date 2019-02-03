# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, render_template
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
commands = {"sub":"sub", "unsub":"unsub"}
@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    number = request.values.get('From', None)
    print("response was: ", body)
   # commands = {"sub": subscribe(number,resp), "unsub": unsubscribe(number,resp)}
    print("\nresponse was from: ", number)
    if body in commands:
        return process(commands[body], number)
    else:
    # Add a message
         resp.message("SALAD: Command not recognized, please try again. (text 'help' for command manual)")
    return str(resp)


def process(command, number):     #this function takes in valid commands and does to the correct action
    resp = MessagingResponse()
    if command == "sub":
        #db.child("numbers").push(str(number))
        db.child("numbers").update({str(number): True})
        resp.message("You have successfully subscribed")
    elif command == "unsub":
        print("unsubscribing " + str(number))
        db.child("numbers").child(str(number)).remove()
        resp.message("You have successfully unsubscribed")
    else:
        resp.message("no action required for command(valid)")
    return str(resp)

def subscribe(number,resp):
    db.child("numbers").update({str(number): True})
    resp.message("You have successfully subscribed")

def unsubscribe(number,resp):
    db.child("numbers").child(str(number)).remove()
    resp.message("You have successfully unsubscribed")

def set_location(location,resp):
    db.child("numbers").child(str(location)).remove()
    resp.message("You have successfully set the location")

@app.route("/contribute")
def index():
    user = {'username':'Person'}
    return render_template('index.html', title='Home', user=user)


if __name__ == "__main__":
    app.run(debug=True)
