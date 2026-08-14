class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tCounts ={}
        sCounts ={}
        for char in s:
            sCounts[char] = sCounts.get(char, 0) + 1
        for char in t:
            tCounts[char] = tCounts.get(char, 0) + 1

        if tCounts == sCounts:
            return True
        return False
        

