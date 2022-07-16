
strs = ["dog","racecar","car"]

str1 = strs[0]

for x in strs[1:]:

    return_str = ""

    i = 0 
    j = 0

    while i < len(str1) and j < len(x) :

        if not str1[i] == x[j]:
            
            break
        else:
            return_str = return_str + str1[i]

        i += 1
        j += 1

    str1 = return_str
    

print(return_str)