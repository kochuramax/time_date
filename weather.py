#api.openweathermap.org/data/2.5/forecast/daily?lat=35&lon=139&cnt=10&appid={API key}
import json

import requests

def get_weather(city):
    print(city)
    weather_key = "bfebbff956c2f268f300d3bed559e225"

    url = 'https://api.openweathermap.org/data/2.5/forecast'

    params = dict(appid=weather_key,q=city,units='metric')

    res = requests.post(url,params=params)
    data_json=json.loads(res.text)
    print(data_json["list"][0]["main"]["temp_min"])
    print(data_json["list"][0]["main"]["temp"])
    print(data_json["list"][0]["main"]["temp_max"])
    print(data_json["list"][0]["main"]["feels_like"])



    return {
        "min_temp":data_json["list"][0]["main"]["temp_min"],
        "max_temp":data_json["list"][0]["main"]["temp_max"],
        "temp": data_json["list"][0]["main"]["temp"],
        "feels_like": data_json["list"][0]["main"]["feels_like"]
    }


