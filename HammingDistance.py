x = 1
y = 4


z = x ^ y

count = 0
while not z == 0:

    lsb = z & 1

    if lsb == 1:
        count = count +1

    z = z >> 1

print(count)
