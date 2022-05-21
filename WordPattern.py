pattern = "abba"
s = "dog cat cat fish"

s_list = s.split(" ")

empty = {}

flag = True

for i in range(len(pattern)):
    if pattern[i] in empty.keys():
        if not empty[pattern[i]] == s_list[i]:
            print("Mismatched item : " + s_list[i])
            flag = False
            break
    else:
        empty[pattern[i]] = s_list[i]

print(f"Is Pattern followed by s : {flag}")
print(f"current dict : {empty}")