class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        unique = []

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key in seen:
            buckets[seen[key]].append(key)
        
        for bucket in reversed(buckets):
            for num in bucket:
                unique.append(num)

            if len(unique) == k:
                return unique
        
        