s = "a#c"
t = "b"

def removehash(str):       
    empty = []
    for x in str :
        if x == "#":
            if not len(empty) == 0:
                empty.pop()
        else:
            empty.append(x)
    return "".join(empty)

str1 = removehash(s)
str2 = removehash(t)

print(str1)
print(str2)

if str1 == str2:
    print("true")
else:
    print("false")
