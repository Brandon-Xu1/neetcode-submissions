class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
            
        output = set()
        new = sorted(nums)
        i = 0
        j = i + 1
        k = len(nums) - 1

        for i in range(len(new)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue 

                total = new[i] + new[j] + new[k]
                if total == 0:
                    output.add((new[i], new[j], new[k]))
                    j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        
        return [list(value) for value in output]            

            
