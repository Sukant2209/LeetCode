s = "b"
t = "abc"

i,j = 0,0

empty = []
while i < len(s) and j < len(t):

    if s[i] == t[j]:
        empty.append(t[j])
        i= i+1
        j=j+1
    else:
        j = j+1

print(s == "".join(empty))


