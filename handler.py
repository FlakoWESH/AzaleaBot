import datetime
import random

hasInit=False
import util.findSticker
import util.weather

STICKER_LIMIT_NUMBER=3

def getStickers(keyword):
    global hasInit
    if not hasInit:
        util.findSticker.init()
        hasInit=True
    result=util.findSticker.lookupInDB(keyword)
    if len(result) > 3:
        result=random.choices(result,k=STICKER_LIMIT_NUMBER)
    return result

normalDescription="城市:{cityName}\n发布时间:{time}\n天气:{weather}\n气温:{temperature:.1f}\n体感温度:{feels_like:.1f}\n"

nativeWarn="气象警告:{content}\n"

def handleNativeWeather(cityName):
    result = util.weather.getNativeWeather(cityName)
    if "error" in result and len(result["error"]) > 0:
        return result["error"]
    time=result["publish_time"]
    temperature=result["weather"]["temperature"]
    feelst=result["weather"]["feelst"]
    info=result["weather"]["info"]
    name=result["station"]["city"]
    content=normalDescription.format(cityName=name,time=time,weather=info,temperature=temperature,feels_like=feelst)
    if "9999" != result["warn"]["alert"]:
        alertContent=result["warn"]["issuecontent"]
        content+=nativeWarn.format(content=alertContent)
    return content

globalExtraInfo="最高气温:{temp_max:.1f}\n最低气温:{temp_min:.1f}\n"

def handleGlobalWeather(cityName):
    result = util.weather.getGlobalWeather(cityName)
    if "error" in result and len(result["error"]) > 0:
        return result["error"]
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    temperature=result["main"]["temp"]
    feels_like=result["main"]["feels_like"]
    info=result["weather"][0]["description"]
    temp_max=result["main"]["temp_max"]
    temp_min=result["main"]["temp_min"]
    name=result["name"]
    content=normalDescription.format(cityName=name,time=time,weather=info,temperature=temperature,feels_like=feels_like)
    content+=globalExtraInfo.format(temp_max=temp_max,temp_min=temp_min)
    return content
