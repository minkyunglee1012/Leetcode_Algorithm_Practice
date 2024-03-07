class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        # print(stack)
        # print(stack[-1])

        for i in range(1, len(s)):
            if not stack:
                stack.append(s[i])

            elif s[i] != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()

        return ''.join(stack)