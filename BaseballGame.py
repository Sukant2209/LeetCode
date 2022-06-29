ops = ["5","-2","4","C","D","9","+","+"]

stack = []

for x in ops:

    if x == "C":
        stack.pop()
    
    elif x == "D":
        double = (stack.pop())
        stack.append((double))
        stack.append((2*double))
    
    elif x == "+":
        second = (stack.pop())
        first = (stack.pop())
        summation = second + first
        stack.append(first)
        stack.append(second)
        stack.append(summation)
    else:
        stack.append(int(x))
    
print(sum(stack))