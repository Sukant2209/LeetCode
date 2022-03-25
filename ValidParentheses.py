

s = input("Enter string....")

def func(s):
    stack=[]
    for x in s:
        if x == "{" or x == "[" or x =="(":
            stack.append(x)
        elif x == "}":
            if "{" in stack:
                stack.remove("{")
        elif x == "]":
            if "[" in stack:
                stack.remove("[")
        elif x == ")":
            if "(" in stack:
                stack.remove(")")

    return True if len(stack)==0 else False

result = func(s)
print(result)