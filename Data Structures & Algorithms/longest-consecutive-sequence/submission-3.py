class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new = set(nums)
        max_count = 1

        for num in nums:
            count = 1
            if num - 1 in new:
                continue
            
            i = 1
            while num + i in new:
                count += 1
                i += 1
            
            max_count = max(max_count, count)

        return max_count
            
            
