input_string = input("Enter you String....")

def isPalindrome(value):
        flag = False
        if len(value) == 1:
            return flag ,0
        if value == value[::-1]:
            flag = True
        return flag , len(value)

def palindrome(s):
    str_ret = None
    temp_val = 0
    length = len(s)
    if length == 1:
        return s
    elif length==2:
        temp_flag , temp_len = isPalindrome(s)
        return s if temp_flag else s[0]
    else:
        for i in range(length):
            for j in range(i+1,length+1):
                temp_flag , temp_len = isPalindrome(s[i:j])
                if temp_flag and temp_len > temp_val:
                    str_ret = s[i:j]
                    temp_val = temp_len
                else:
                    continue
        return str_ret if str_ret else s[0]
          
        
result = palindrome(input_string)  
print(result)
