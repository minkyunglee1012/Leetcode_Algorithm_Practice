class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if '.' not in logs[i]:
                stack.append(logs[i])
            if '..' in logs[i] and stack:
                stack.pop()
            if '.' in logs[i] and '..' not in logs[i]:
                pass
            
        return len(stack)