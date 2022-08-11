stickerPath="resource/sticker/"

stickFolder=["snow miku/","SNOW MIKU 2017&Yukine(HATSUNE MIKU)_4994420_sticker/","洛天依/","初音未来周年纪念/","未来有你/"]

DB={}

import os

def getAllStickers(path):
    dir_list = os.listdir(path)
    allFiles= [path + s for s in dir_list]
    return list(filter(lambda file: os.path.isfile(file), allFiles))


def handleOneFile(filename):
    def addIntoDB(tag,filename):
        if tag not in DB:
            DB[tag]=[]
        DB[tag].append(filename)
    names=os.path.splitext(filename)
    stickerTags=names[0].split("_")
    for tag in stickerTags:
        addIntoDB(tag,filename)
    addIntoDB(names[1][1:],filename)

def lookupInDB(tag):
    result=[]
    for key in DB.keys():
        if tag in key:
            result+=DB[key]
    return result

def init():
    for folder in stickFolder:
        for stick in getAllStickers(stickerPath+folder):
            handleOneFile(stick)