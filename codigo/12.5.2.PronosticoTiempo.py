import requests
r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Granada&appid=YOUR_API_KEY").json()
description = r["weather"][0]["description"]
temp = r["main"]["temp"] - 273.15
mainWeather = r['weather'][0]['main']