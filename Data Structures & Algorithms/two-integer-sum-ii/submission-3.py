class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new = sorted(numbers)
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = new[left] + new[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        

                