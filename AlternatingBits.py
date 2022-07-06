n = 10

lsb = n & 1
flag = False
while not n == 0:
    
    n = n >> 1

    new_lsb = n & 1
    
    if lsb == new_lsb:
        flag = True
        break
    else:
        lsb = new_lsb

print(flag)