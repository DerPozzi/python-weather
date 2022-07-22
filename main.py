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

emoji = choose_emoji(weather["main"])

if emoji == None:
    emoji = ""

sunrise = str(strftime("%H:%M:%S", gmtime(json["sys"]["sunrise"] + json["timezone"])))
sunset = str(strftime("%H:%M:%S", gmtime(json["sys"]["sunset"] + json["timezone"])))


print(f"\n=========================================={location}============================================\n")
print(f"Das aktuelle Wetter in {location} ist {emoji}{weather['description']}. Die Temperatur beträgt {main['temp']}°C.")
print(f"Die Luftfeuchtigkeit beträgt {main['humidity']}% und der Luftdruck liegt bei {main['pressure']}hPa.")
print(f"Sonnenaufgang: {sunrise} Uhr")
print(f"Sonnenuntergang: {sunset} Uhr")
print("\n===========================================================================================")
