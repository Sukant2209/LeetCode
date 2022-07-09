
s = "(())((()))"

stack = []
count = count_dracula = 0

str1 = ""
str2=""
for x in s:
    
    str1 = str1 + x
    
    if x == "(" : count = count +1
    if x == ")" : count_dracula += 1

    if count == count_dracula:
        temp= str1[1:len(x)-1]
        str2 = str2 + temp
        str1 = ""

print(stack)
print(str2)