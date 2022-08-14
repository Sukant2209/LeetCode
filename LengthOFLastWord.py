s = "hello world"

s = s.strip()

count = 0

for i in range(len(s)-1,-1,-1):
    count = count + 1
    
    if s[i] == "":
        break

print(count)