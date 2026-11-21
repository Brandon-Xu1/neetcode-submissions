class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        left = 0
        right = len(heights) - 1
        total = 0

        while left < right:
            total = max(min(heights[right], heights[left]) * (right - left), total)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return total
