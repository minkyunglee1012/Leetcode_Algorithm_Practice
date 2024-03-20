class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for ch in operations:

            if ch not in 'CD+':
                stack.append(int(ch))

            elif ch == 'C':
                stack.pop()

            elif ch == 'D':
                stack.append(stack[-1] * 2)

            elif ch == '+':
                stack.append(stack[-1] + stack[-2])

        answer = sum(stack)

        return answer
