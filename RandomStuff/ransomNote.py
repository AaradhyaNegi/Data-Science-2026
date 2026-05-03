class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = Counter(magazine)

        for i in ransomNote:
            if d1[i] == 0:
                return False
            d1[i] -= 1    

        return True