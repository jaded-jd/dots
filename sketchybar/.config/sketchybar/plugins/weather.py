import requests as r
import os
import geocoder

#os.system(f'sketchybar --set weather label="Loading"')

g = geocoder.ip('me')
lat, lon = g.latlng

# Define your API key and location
API_KEY = '74e7682f4f0a47cbb07130046241106'
URL = f'https://api.weather.com/v1/current.json?q=melbourne&key={API_KEY}'
# Fetch weather information
response = r.get(f"https://api.weatherapi.com/v1/current.json?q={lat},{lon}&key=34d710b999a845a2883131334241106")
data = response.json()
# Define the condition to icon mapping
weather_icons = {
    "cloud": "󰖐",
    "fog": "󰖑",
    "hail": "󰖒",
    "hazy": "󰼰",
    "hurricane": "󰢘",
    "lightning": "󰖓",
    "night": "󰖔",
    "overcast": "",
    "pouring": "󰖖",
    "rain": "󰖗",
    "snow": "󰖘",
    "sunny": "󰖙",
    "sunset": "󰖚",
    "tornado": "󰼸",
    "wind": "󰖝"
}

# Get weather condition
weather_condition = data['current']
temp = weather_condition['temp_c']
conditions = weather_condition['condition']['text']
print(conditions)

icon = conditions
for k,v in weather_icons.items():
    if k.lower() in conditions.lower():
        icon = v

#print(conditions)
os.system(f'sketchybar --set weather icon="{icon}" label="{temp}°C"')
