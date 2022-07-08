s = "()[]{}"

def validParenthesis(s): 
    stack = []   
    for x in s:
        
        if x == "(" or x == "[" or x =="{" :
            stack.append(x)
        
        else:
            if len(stack) == 0:
                stack.append(x)
            else:
                last_element = stack.pop()
                if not (last_element + x) == "()" and not (last_element + x) == "[]" and not (last_element + x) == "{}":
                    return False
            
    return len(stack) == 0 

res = validParenthesis(s)
print(res)