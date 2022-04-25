# binary_num = 1000
decimal_num =5

# def convertToNum(binary_num):
#     num = 0
#     power = 0
#     while binary_num >= 1:
#         q = binary_num % 10
#         binary_num  = binary_num // 10
#         if q == 1:
#             num= num+ 2**power
#         power = power +1
#     return num

# result = convertToNum(binary_num)
# print(result)

def convertToBinary(decimal_num):
        num = 0
        power=0
        while decimal_num >= 1:
            q = decimal_num % 2
            decimal_num  = decimal_num // 2
            if q == 1:
                num= num+ 10**power
            power = power +1
        return num

result = convertToBinary(decimal_num)
print(result)
