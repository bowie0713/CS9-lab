from lab03 import multiply
from lab03 import collectMultiples
from lab03 import countVowels
from lab03 import reverseVowels
from lab03 import removeSubString

def test_multiply():
    assert multiply(5,4) == 20
    assert multiply(0,5) == 0
    assert multiply(3,6) == 18
    assert multiply(0,0) == 0
    assert multiply(10,5) == 50
    assert multiply(15,4) == 60
def test_collectMultiples():
    assert collectMultiples([1,3,5,7,9], 3) == [3,9]
    assert collectMultiples([2,4,5,6,9], 2) == [2,4,6]
    assert collectMultiples([2,3,5,7,9], 11) == []
    assert collectMultiples([10, 11, 13, 7, 5], 2) == [10]
def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("My name is Bowie") == 6
    assert countVowels("12345678") == 0
    assert countVowels("i am not Becker") == 5
    assert countVowels("I LOVE UCSB") == 4
def test_reverseVowels():
    assert reverseVowels("Eunoia") == "aiouE"
    assert reverseVowels("My name is Bowie") == "eioiea"
    assert reverseVowels("sdfghjk") == ""
    assert reverseVowels("123456") == ""
    assert reverseVowels("UCSB") == "U"
def test_removeSubString(): 
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("My name is Bowie", "e") == "My nam is Bowi"
    assert removeSubString("MISSISSIPPI", "IS") == "MSSIPPI"
    assert removeSubString("MISSISSIPPI", "is") == "MISSISSIPPI"
    assert removeSubString("MISSISSIPPI", "MISSISSIPPI") == ""
#print(removeSubString("MISSISSIPPI", "MISSISSIPPI"))

