class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False
        
        window = {}
        target = {}

        for char in s1:
            target[char] = target.get(char, 0) + 1
        
        for char in s2[:m]:
            window[char] = window.get(char, 0) + 1
        
        if window == target:
            return True
        
        for right in range(m, n):
            char = s2[right]
            window[char] = window.get(char, 0) + 1

            old = s2[right - m]
            window[old] -= 1

            if window[old] == 0:
                del window[old]
            
            if window == target:
                return True
        
        return False


