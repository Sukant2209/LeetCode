prices = [7,1,5,3,6,4]

empty = []
def myfunc(prices):

    if len(prices) == 0:
        return
    stock_buy = prices[0]

    for x in prices[1:]:
        if x > stock_buy:
            empty.append(x-stock_buy)

    return myfunc(prices[1:])

myfunc(prices)
print(empty)


# l, r = 0, 1 
# maxP = 0
# while r < len(prices):
#     if prices[l] < prices[r]:
#         profit = prices[r] - prices[l]
#         maxP = max ( maxP, profit)
#     else:
#         l = r
#     r = r+1
# print(maxP)




