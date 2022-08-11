import os.path

import util.findSticker

testCase=["SNOW MIKU 2017"]

def testInit():
    util.findSticker.stickerPath=util.findSticker.stickerPath

def test():
    testInit()
    util.findSticker.init()
    for str in testCase:
        result=util.findSticker.lookupInDB(str)
        for file in result:
            assert os.path.isfile(file)

test()