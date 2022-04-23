
stones = [7,8,3]

def games(stones):
    len_stones = len(stones)

    if len_stones == 0:
        return 0
    elif len_stones == 1:
        return stones[0]
    else:
        stones.sort()
        i = len(stones)-1
        j = i-1
        counter = 0
        
        if stones[i] == stones[j]:
            stones.pop();stones.pop()
            return games(stones)
        else:
            counter = stones[i] - stones[j]
            stones.pop();stones.pop()
            stones.append(counter)
            return games(stones)

result = games(stones)
print(result)
