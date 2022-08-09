hasInit=False
import util.findSticker

def getStickers(keyword):
    global hasInit
    if not hasInit:
        util.findSticker.init()
        hasInit=True
    return util.findSticker.lookupInDB(keyword)
