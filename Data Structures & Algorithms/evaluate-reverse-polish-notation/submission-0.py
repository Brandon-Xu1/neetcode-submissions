class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for num in tokens:
            if num not in ['+', '-', '*', '/']:
                stack.append(int(num))
            else:
                b = stack.pop()
                a = stack.pop()

                if num == '+':
                    stack.append(a + b)
                elif num == '-':
                    stack.append(a - b)
                elif num == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

        return stack[-1]