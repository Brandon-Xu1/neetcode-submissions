class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        stack = []

        for char in s:
            if char in check and stack:
                if check[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
                