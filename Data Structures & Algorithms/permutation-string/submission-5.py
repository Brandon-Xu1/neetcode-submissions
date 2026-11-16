class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        i = 0

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        while i + len(s1) <= len(s2):
            s1_copy = s1_dict.copy()
            for j in range(i, i + len(s1)):
                if s2[j] in s1_copy:
                    s1_copy[s2[j]] -= 1
                else:
                    break
            
            if all(value == 0 for value in s1_copy.values()) == True:
                return True

            i += 1
            
        
        return False