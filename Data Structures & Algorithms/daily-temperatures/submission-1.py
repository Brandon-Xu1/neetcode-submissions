class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append(index)
                continue
            
            while stack and temp > temperatures[stack[-1]]:
                old = stack.pop()
                result[old] += index - old
            
            stack.append(index)
        
        return result