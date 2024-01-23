def multiply(x, y):
    if x * y == 0:
        return 0
    return x + multiply(x, y-1)

def collectMultiples(intList, n):
    if len(intList) == 0:
        return []
    if intList[len(intList)-1] % n == 0:
        a = intList.pop()
        return collectMultiples(intList, n) + [a]
    intList.pop()
    return collectMultiples(intList, n)

#print(collectMultiples([2,4,6,7,8], 2))

def countVowels(s):
    if len(s) == 0:
        return 0
    if 'A' in s[len(s)-1].upper() or 'E' in s[len(s)-1].upper() or 'I' in s[len(s)-1].upper() or 'O' in s[len(s)-1].upper() or 'U' in s[len(s)-1].upper():
        s = s.rstrip(s[-1])
        return 1 + countVowels(s)
    s = s.rstrip(s[-1])
    return countVowels(s)
#print(countVowels("This Is A String"))
def reverseVowels(s):
    if len(s) == 0:
        return ""
    if 'A' in s[len(s)-1].upper() or 'E' in s[len(s)-1].upper() or 'I' in s[len(s)-1].upper() or 'O' in s[len(s)-1].upper() or 'U' in s[len(s)-1].upper():
        return s[len(s)-1] + reverseVowels(s.rstrip(s[-1]))
    return reverseVowels(s.rstrip(s[-1]))
#print(reverseVowels("Eunoia"))

def removeSubString(s, sub):
    if sub not in s:
        return s
    idx = s.find(sub)
    new = s[:idx] + s[idx+len(sub):] #from 0 to the index that found the sub string, then add substring length to get the rest of the s string.
    return removeSubString(new, sub)
#print(removeSubString("Lolololol", "lol"))