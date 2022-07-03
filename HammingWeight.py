
n = 0b00000000000000000000000000001011

print(n)

count = 0
while not n == 0:

    if n & 1 == 1:
        
        count += 1

    n = n >> 1


print(count)