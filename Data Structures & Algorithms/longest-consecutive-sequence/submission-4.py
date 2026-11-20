class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new = set(nums)
        count = 1
        max_count = 1

        for num in new:
            if num - 1 in new:
                continue
            
            while num + 1 in new:
                count += 1
                num += 1
            
            max_count = max(max_count, count)
            count = 1
        

        return max_count

