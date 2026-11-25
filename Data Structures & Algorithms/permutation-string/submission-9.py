class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)
        check = {}
        window = {}
        for char in s1:
            check[char] = check.get(char, 0) + 1
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        while right < len(s2):
            if window == check:
                return True
            else:
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]
                window[s2[right]] = window.get(s2[right], 0) + 1
            
            left += 1
            right += 1
        
        return window == check
        

