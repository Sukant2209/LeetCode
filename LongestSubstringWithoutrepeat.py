str = "abcabcbb"
#Find the substring


def longest(str):
    if str=="":
        return 0
    empty = [1]
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[j] in str[i:j]:
                break
            else:
                empty.append(len(str[i:j]+str[j]))
   
            
    return max(empty)

res=longest(str)
print(res)
# print(empty[len(empty)-1])

# class Solution:
# 	def lengthOfLongestSubstring(self, s: str) -> int:
# 	"""
# 	Let's write what we see to dictionary
# 	And track left, right border of our not repeated char. substring
# 	"""
# 		seen = {}
# 		max_length = left = right = 0
# 		for idx, value in enumerate(s):
# 			if value in seen:
# 			# Cause we seen repeated character, we need to choose new left border
# 				left = max(seen[value] + 1, left)
				
# 			seen[value] = idx
# 			# Move right border
# 			right = idx
# 			# Calc max lehgth
# 			max_length = max(right - left + 1, max_length)
				
# 		return max_length