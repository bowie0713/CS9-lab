from Week_3 import biggestInt

def test_biggestInt1(): #need to start with test_
    assert biggestInt(1,2,3,4) == 4
    assert biggestInt(1,2,4,3) == 4
    assert biggestInt(1,4,2,3) == 4
    assert biggestInt(4,1,2,3) == 4
def test_biggestInt2():
    assert biggestInt(5,5,5,5) == 5
def test_biggestInt3():
    assert biggestInt(-5, -10, -12, -1000) == -5
    assert biggestInt(-100, 1, 100, 0) == 100
    
    