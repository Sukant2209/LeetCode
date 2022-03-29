s = input("Enter you String....")

def isPalindrome(value):
        flag = False
        if value == value[::-1]:
            flag = True
        return flag , len(value)

def palindrome(s):

    length = len(s)
    l_dict = {}
    if length == 1:
            return s[0]
    elif length == 2:
            return s if s==s[::-1] else s[0]
    else:
        for i in range(length):
            for j in range(i+1,length+1):
                temp_flag , temp_len = isPalindrome(s[i:j])
                if temp_flag :
                    l_dict[s[i:j]] = temp_len
                else:
                    continue
        return max(l_dict, key= lambda x: l_dict[x])
          
        
result = palindrome(s)
print(result)
