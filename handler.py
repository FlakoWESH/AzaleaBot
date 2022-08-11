import random

hasInit=False
import util.findSticker

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
