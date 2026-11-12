class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for j in t:
            if j in seen:
                seen[j] -= 1
            else:
                return False

        return all(value == 0 for value in seen.values())
