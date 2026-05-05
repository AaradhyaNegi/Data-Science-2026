# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         d1 = Counter(magazine)

#         for i in ransomNote:
#             if d1[i] == 0:
#                 return False
#             d1[i] -= 1    

#         return True


set_a = {1,2,3,4,5}
set_b = {2,3,5,6,7}

print(set_a ^ set_b)