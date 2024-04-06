class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for idx, val in enumerate(s):
            if val == '(':
                stack.append(idx)
            elif val == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(idx)

        result = []
        for idx, val in enumerate(s):
            if stack and idx == stack[0]:
                stack.pop(0)
                continue
            result.append(val)

        return ''.join(result)