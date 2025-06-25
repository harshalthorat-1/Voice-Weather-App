import requests
import json
import os
import pyttsx3


while True:

    city_name = input('Enter City Name: ')
    key = '9e3f13be34e148c6a4f94522252506'
    url =f'http://api.weatherapi.com/v1/current.json?key=9e3f13be34e148c6a4f94522252506&q={city_name}'

    r = requests.get(url)
    # print(r.text)
    wdict = json.loads(r.text)

    temp = (wdict["current"]["temp_c"])
    text_say = f'The weather in {city_name} is {temp}'
    if city_name == "bye":
        break
    engine = pyttsx3.init()
    engine.say(text_say)
    print(f"The weather in {city_name} is {temp}")
    engine.runAndWait()
