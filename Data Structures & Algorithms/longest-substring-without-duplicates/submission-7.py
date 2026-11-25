class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        max_length = 1
        left = 0
        right = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            right += 1
            max_length = max(max_length, len(seen))

        return max_length
