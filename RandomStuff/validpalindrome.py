# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s1 = ''.join(ch for ch in s if ch.isalnum()).strip().lower()
#         left, right = 0 , len(s1) - 1 

#         while left <= right:
#             if s1[left] != s1[right]:
#                 return False
#             left += 1
#             right -= 1
    
#         return True

s = "A man, a plan, a canal: Panama"
s1 = ''.join(ch for ch in s if ch.isalnum()).strip().lower()
print(s)
print(s1[::-1])