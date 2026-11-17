class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            ')' : '(',
            ']' : '[',
            '}' : '{'  
        }
        
        stack = []

        for char in s:
            if char in key and stack:
                if key[char] != stack[-1]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(char)

        return len(stack) == 0