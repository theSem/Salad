import requests
from datetime import datetime

POSTAL_CODE = '92274'
WEATHERBIT_KEY = '2573254dc43e4b1cbbb895739aafcc95'
AERIS_ID = '5yCPVOV7ClmYRoF4RSbmB'
AERIS_SECRET = 'Ergc2GajB2wYwdiLMd4ily0sBknJVgSZDZ7NngGE'

def weatherUpdate():
    weatherbit = requests.get("https://api.weatherbit.io/v2.0/forecast/daily?postal_code={0}&key={1}".format(POSTAL_CODE, WEATHERBIT_KEY))
    bitData = weatherbit.json()['data']
    for day, weather in enumerate(bitData):
        print(day + 1, ": ", weather['weather']['description'])

def advisoryUpdate():
    aerisweather = requests.get("https://api.aerisapi.com/alerts/{0}?&format=json&limit=10&client_id={1}&client_secret={2}".format(POSTAL_CODE, AERIS_ID, AERIS_SECRET))
    aerisData = aerisweather.json()['response']

    try:
        print(aerisData[0]['details']['body'])
    except:
        print("No current weather advisories.")


def droughtUpdate():
    drought = requests.get("https://api.aerisapi.com/droughts/monitor/{0}?client_id={1}&client_secret={2}".format(POSTAL_CODE, AERIS_ID, AERIS_SECRET))
    droughtData = drought.json()

    try:
        droughtStuff = droughtData['response'][0]['details']
        droughtStatus = droughtStuff['risk']['name']
        print(droughtStatus)
        print("Issued until: ", datetime.utcfromtimestamp(droughtStuff['range']['maxTimestamp']).strftime('%Y-%m-%d %H:%M:%S'))
    except:
        print("No current drought risk.")
