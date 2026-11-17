class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):

            if not stack:
                stack.append(index)
                continue
            
            while stack and temp > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] += index - previous_index
                

            stack.append(index)
           
            
        return result

