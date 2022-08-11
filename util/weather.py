import json

import requests
from botpy.ext.cog_yaml import read
import os

weather_config = None
apiKey=None
defaultLang="zh_cn"
defaultUnits="metric"
cityCode=None
url="https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&lang={lang}&units={units}"
nativeUrl="http://www.nmc.cn/f/rest/real/{cityCode}"
NOT_FOUND_ERROR={"error":"无法找到查询城市"}
OTHER_ERROR={"error":"错误发生，无法查询"}


def init():
    global weather_config
    global apiKey
    global cityCode
    if weather_config is None:
        weather_config=read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
        apiKey=weather_config['weather_key']
    if cityCode is None:
        with open("resource/weather/cityCode",encoding="utf-8") as fin:
            cityCode=json.load(fin)

def getNativeWeather(cityName):
    if cityCode is None:
        init()
    if cityName not in cityCode:
        for city in cityCode.keys():
            if cityName in city:
                cityName=city
                break

    if cityName in cityCode:
        code=cityCode[cityName]
        response=requests.get(nativeUrl.format(cityCode=code))
        if response.status_code !=200:
            return OTHER_ERROR
        return response.json()
    else:
        return NOT_FOUND_ERROR

def getGlobalWeather(cityName):
    if apiKey is None:
        init()
    realUrl=url.format(cityName=cityName,apiKey=apiKey,lang=defaultLang,units=defaultUnits)
    response=requests.get(realUrl)
    if response.status_code == 404:
        return NOT_FOUND_ERROR
    elif response.status_code != 200:
        return OTHER_ERROR
    else:
        return response.json()
