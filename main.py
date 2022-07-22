import sys
import requests
from geopy.geocoders import Nominatim
import json
from time import strftime 
from time import gmtime
import datetime

def choose_emoji(weather):
    match weather:
        case "Cloudy":
            return "🌤"
        case "Sunny":
            return "☀"
        case "Rain":
            return "🌧"
        case "Snow":
            return "🌨"
        

apiKey = "95b5a2960c4a91337c38d65b39d55cfb"

geolocator = Nominatim(user_agent="MyApp")

location = sys.argv[1]
location_coord = geolocator.geocode(location)
lat = location_coord.latitude
lon = location_coord.longitude

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=de&appid={apiKey}&units=metric"
res = requests.get(url)
json = res.json()
weather = json["weather"][0]
main = json["main"]
sys = json ["sys"]

data = {
    "description" : weather['description'],
    "temp" : main["temp"],
    "humidity" : main["humidity"],
    "pressure" : main["pressure"],
    "sunset" : sys["sunset"],
    "sunrise" : sys["sunrise"],
    "deltatime" : json["timezone"]
}


emoji = choose_emoji(weather["main"])

if emoji == None:
    emoji = ""

sunrise = str(strftime("%H:%M:%S", gmtime(data["sunrise"] + data["deltatime"])))
sunset = str(strftime("%H:%M:%S", gmtime(data["sunset"] + data["deltatime"])))


print(f"\n=========================================={location}============================================\n")
print(f"Das aktuelle Wetter in {location} ist {emoji}{data['description']}. Die Temperatur beträgt {data['temp']}°C.")
print(f"Die Luftfeuchtigkeit beträgt {data['humidity']}% und der Luftdruck liegt bei {data['pressure']}hPa.")
print(f"Sonnenaufgang: {sunrise} Uhr")
print(f"Sonnenuntergang: {sunset} Uhr")
print("\n===========================================================================================")
