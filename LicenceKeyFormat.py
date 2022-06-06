s = "2-5g-3-J"
k = 2

str = "".join(s.split("-"))
l_str = len(str)
empty = []

def licence(str, k):
    for i in range(0,len(str),k):
        str1 = str[i:i+k]
        empty.append(str1)

if l_str % k == 0:
    licence(str,k)
else:
    m = l_str % k
    print(m)
    str2 = str[0:m]
    str3 = str[m:]
    empty.append(str2)
    licence(str3,k)


print("-".join(empty).upper())

