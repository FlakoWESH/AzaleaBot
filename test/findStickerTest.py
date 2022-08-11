import os.path

import util.findSticker

testCase=["SNOW MIKU 2017","洛天依"]

def test():
    util.findSticker.init()
    for str in testCase:
        result=util.findSticker.lookupInDB(str)
        assert len(result) != 0
        for file in result:
            assert os.path.isfile(file)

test()