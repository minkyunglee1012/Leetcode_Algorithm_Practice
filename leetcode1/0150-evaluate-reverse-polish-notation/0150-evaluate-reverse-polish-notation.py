class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 아래에 코드를 작성해주세요.
        stack = []

        for ch in tokens:
            if ch not in '+-*/':
                stack.append(int(ch))
            else:
                if ch == '+':
                    s1 = stack.pop()
                    s2 = stack.pop()
                    stack.append(s2 + s1)
                elif ch == '-':
                    s3 = stack.pop()
                    s4 = stack.pop()
                    stack.append(s4 - s3)
                elif ch == '*':
                    s5 = stack.pop()
                    s6 = stack.pop()
                    stack.append(s6 * s5)
                elif ch == '/':
                    s7 = stack.pop()
                    s8 = stack.pop()
                    stack.append((s8 / s7).__trunc__())

        return sum(stack)