ransomNote="a"
magazine = "b"
 
def canMake(ransomNote, magazine):
    rnDict = {}
    mDict = {}

    for x in ransomNote:
        if x not in rnDict:
            rnDict[x] = 1
        else:
            rnDict[x] += 1

    for x in magazine:
        if x not in mDict:
            mDict[x] = 1
        else:
            mDict[x] += 1
            
    for x in rnDict.keys():
        if x in mDict:
            if not mDict[x] >= rnDict[x]:
                return False
        else:
            return False

    return True

print(canMake(ransomNote, magazine))