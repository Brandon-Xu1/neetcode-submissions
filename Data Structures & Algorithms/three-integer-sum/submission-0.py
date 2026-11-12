class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        sorted_nums = sorted(nums)

        i = 0
        j = 0
        k = len(sorted_nums) - 1

        storage = set()

        while i < len(sorted_nums) - 1:
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue

                target = -sorted_nums[i]
                value = sorted_nums[j] + sorted_nums[k]
        
                if target == value:
                    storage.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                elif value < target:
                    j += 1
                else:
                    k -= 1
            i += 1
            j = i + 1
            k = len(sorted_nums) - 1
        
        return [list(triplet) for triplet in storage]
                

