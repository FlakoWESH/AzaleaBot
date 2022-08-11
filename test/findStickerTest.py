import os.path

import handler

testCase=["SNOW MIKU 2017","洛天依"]

def test():
    for str in testCase:
        result=handler.getStickers(str)
        assert len(result) > 0 and len(result) <= 3
        for file in result:
            assert os.path.isfile(file)

test()