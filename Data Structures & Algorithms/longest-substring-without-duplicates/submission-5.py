class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_count = 0
        check = set()
        
        for right in range(len(s)):
            
            while s[right] in check:
                check.remove(s[left])
                left += 1

            check.add(s[right])
            max_count = max(max_count, len(check))

        return max_count