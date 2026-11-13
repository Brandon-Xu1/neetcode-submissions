class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            
            while (right - left + 1) - max(count.values()) > k:
                if count[s[left]] == 1:
                    del count[s[left]]
                else:
                    count[s[left]] -= 1

                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length