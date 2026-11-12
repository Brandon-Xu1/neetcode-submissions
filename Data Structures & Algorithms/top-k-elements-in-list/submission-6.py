class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for i in seen:
            buckets[seen[i]].append(i)
        
        final = []
        for bucket in reversed(buckets):
            for num in bucket:
                final.append(num)
                if len(final) == k:
                    return final
                
