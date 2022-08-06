stickFolder=["snow miku/","SNOW MIKU 2017&Yukine(HATSUNE MIKU)_4994420_sticker/","洛天依"]

DB={}

import os

def getAllStickers(path):
    dir_list = os.listdir(path)
    return dir_list

def handleOneFile(filename):
    def addIntoDB(tag,filename):
        if tag not in DB:
            DB[tag]=[]
        DB[tag].append(filename)
    names=os.path.splitext(filename)
    stickerTags=names[0].split("-")
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
        for stick in getAllStickers(folder):
            handleOneFile(stick)

def main():
    init()
    print("init.... done")
    while(True):
        tag=input()
        print(lookupInDB(tag))

main()