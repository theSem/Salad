# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
import pyrebase 
from weather import weatherUpdate
import time

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

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    body = body.lower()
    number = request.values.get('From', None)
    (command,var) = parse_message(body)
    print("response was: ", body)
    print("command was: ", command)
    twocommands = {"signup":signup, "leave":leave, "weather":getweather, "manual":manual}
    threecommands = {"sub":subscribe, "unsub": unsubscribe, "setzip": set_location}
    print("\nresponse was from: ", number)
    if command in twocommands:
        return twocommands[command](number,resp)
    elif command in threecommands:
        return threecommands[command](number,var,resp)
    else:
    # Add a message
        resp.message("Farmer SMS: Command not recognized, please try again. (text 'manual' for command manual)")
        return str(resp)

def process(command, number):     #this function takes in valid commands and does to the correct action
    resp = MessagingResponse()
    return str(resp)

def parse_message(message):
    words = message.split(" ")
    if len(words) == 1:
        return (words[0],None)
    else:
        return (words[0],words[1])

def signup(number,resp):
    db.child("numbers").update({str(number): True})
    resp.message("You have successfully subscribed")
    print("signup")
    return str(resp)

def leave(number,resp):
    db.child("numbers").update({str(number): False})
    resp.message("You have successfully unsubscribed")
    print("leave")
    return str(resp)

def subscribe(number, var, resp):
    db.child("services").child(str(var)).update({str(number):True})
    message = "You have successfully subscribed to the {0} service.".format(var)
    print("subscribe")
    resp.message(message)
    return str(resp)

def unsubscribe(number, var, resp):
    db.child("services").child(str(var)).update({str(number):True})
    message = "You have successfully unsubscribed from the {0} service.".format(var)
    resp.message(message)
    print("unsubscribe")
    return str(resp)

def set_location(number,location,resp):
    db.child("locations").update({str(number):str(location)})
    resp.message("You have successfully set the location")
    return str(resp)

def getweather(number, resp):
    locations = db.child("locations").get()
    if number in locations.val():
        text = weatherUpdate(locations.val()[number])
        resp.message(text)
    else:
        text = "You must set your location before receiving weather updates."
        resp.message(text) 
    return str(resp)

def manual(number, resp):
    text = "sub weather: Sign up of daily weather updates. \n unsub: Unsubscribe for weather updates. \n weather: Get 16 day weather forcaset \n setzip [zipcode]: Set zip-code for location-based weather services "
    resp.message(text)
    return str(resp)

@app.route("/farmersms")
def index():
    user = {'username':'Person'}
    return render_template('index.html', title='Home', user=user)


if __name__ == "__main__":
    app.run(debug=True)




