s = "A man, a plan, a canal: Panama"


i =0
j = len(s) - 1

flag = True
while i<j:
    
    if s[i].lower() == s[j].lower():
        i += 1
        j -= 1
    elif not s[i].isalnum():
        i += 1
    elif not s[j].isalnum():
        j -= 1
    else:
        flag = False
        break

print(flag)  
