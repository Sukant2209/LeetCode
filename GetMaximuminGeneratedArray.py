
n = 7
empty = []

def myfunc(n, memo={}):
        
    
    if n in memo : return memo[n]
    
    if n == 0 : return 0
    if n == 1 : return 1
    
    if not n % 2 == 0: memo[n] = myfunc(n//2) + myfunc((n//2) +1)
    else: memo [n] = myfunc(n // 2)
        
    empty.append(memo[n])

    return memo[n]


for i in range(n+1):
    myfunc(i)

print(empty)
