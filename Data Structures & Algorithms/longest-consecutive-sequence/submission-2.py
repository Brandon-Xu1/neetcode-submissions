class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new = set(nums)
        maxCount = 1

        for num in new:
            count = 1
            if num - 1 in new:
                continue
            
            i = 1
            while num + i in new:
                i += 1
                count += 1
                
            maxCount = max(maxCount,count)
        
        return maxCount