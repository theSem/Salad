import requests
response = requests.get("https://api.weatherbit.io/v2.0/current?postal_code=55414&key=2573254dc43e4b1cbbb895739aafcc95")
data = response.json()
print("Date: ", data['data'][0]['datetime'])
print("Sunrise: ", data['data'][0]['sunrise'])
print("Sunset: ", data['data'][0]['sunset'])
print("Desc: ", data['data'][0]['weather']['description'])
print("City: ", data['data'][0]['city_name'])
