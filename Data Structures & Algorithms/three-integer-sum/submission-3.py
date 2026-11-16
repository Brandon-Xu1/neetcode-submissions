class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        sorted_nums = sorted(nums)
        
        i = 0
        j = i + 1
        k = len(nums) - 1

        output = set()
        
        while i < len(nums) - 1:
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue
            
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                if total == 0:
                    output.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

            i += 1
            j = i + 1
            k = len(nums) - 1
        return [value for value in output]