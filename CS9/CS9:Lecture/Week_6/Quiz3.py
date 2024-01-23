def f(n):
    if n > 500:
        return 0
    else:
        return f(n+1)
print(f(200))
def f2(n):
    if n <= 0:
        return 0
    return 1 + f(n // 2)
print(f2(200))

def removeVowels(s):
    find = "AEIOU"
    if len(s) == 0:
        return s
    if s[0].upper() in find:
        return removeVowels(s[1:])
    return s[0] + removeVowels(s[1:])
    

print(removeVowels("CS9"))
print(removeVowels("Audio"))

def test_removeVowels():
    assert removeVowels("") == ""
    assert removeVowels("CS9") == "CS9"
    assert removeVowels("U") == ""
    assert removeVowels("Audio") == "d"
    assert removeVowels("Mississippi") == "Msssspp"
        