import sys
import requests
from geopy.geocoders import Nominatim
import json
from time import strftime 
from time import gmtime
from tabulate import tabulate
from time import sleep

apiKey = "d54304ec664dc8d46491e6b29540f2bf"

geolocator = Nominatim(user_agent="MyApp")

location = sys.argv[1]
location_coord = geolocator.geocode(location)
lat = location_coord.latitude
lon = location_coord.longitude

#Current weather info for the location

current_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=de&appid={apiKey}&units=metric"

current_res = requests.get(current_url)
json = current_res.json()
weather = json["weather"][0]
main = json["main"]
system = json ["sys"]

current_data = {
    "description" : weather['description'],
    "temp" : main["temp"],
    "humidity" : main["humidity"],
    "pressure" : main["pressure"],
    "sunset" : system["sunset"],
    "sunrise" : system["sunrise"],
    "deltatime" : json["timezone"]
}


# Airpollution

pollution_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={apiKey}"
pollution_res = requests.get(pollution_url)
pollution_json = pollution_res.json()
components = pollution_json["list"][0]["components"]

pollution_data = {
   "index" : pollution_json["list"][0]["main"]["aqi"],
   "co" : components["co"],
   "no" : components["no"],
   "no2" : components["no2"],
   "o3" : components["o3"],
   "pm2_5" : components["pm2_5"],
   "nh3" : components["nh3"]
}

print(pollution_data)

sunrise = str(strftime("%H:%M:%S", gmtime(current_data["sunrise"] + current_data["deltatime"])))
sunset = str(strftime("%H:%M:%S", gmtime(current_data["sunset"] + current_data["deltatime"])))

table = [["Angaben in μg/m3", pollution_data['co'], pollution_data['o3'], pollution_data['no'], pollution_data['no2'], pollution_data['nh3'], pollution_data['pm2_5']],["Airquality Index", pollution_data['index']]]


print(f"\n========================================== {location} Wetter =========================================================\n")
sleep(2)
print(f"Das aktuelle Wetter in {location} ist {current_data['description']}. Die Temperatur beträgt {current_data['temp']}°C.")
print(f"Die Luftfeuchtigkeit beträgt {current_data['humidity']}% und der Luftdruck liegt bei {current_data['pressure']}hPa.")
sleep(1)
print(f"Sonnenaufgang: {sunrise} Uhr")
print(f"Sonnenuntergang: {sunset} Uhr")
print(f"\n========================================== {location} Luftqualität ================================================== \n")
sleep(1)
print(tabulate(table, headers=["", "CO²", "Ozon", "NO", "NO²", "Ammoniak", "Feinstaub"]))