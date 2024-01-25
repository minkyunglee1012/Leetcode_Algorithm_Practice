class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            
            elif ch == ')':
                if not stack:
                    return False
                elif '(' not in stack:
                    return False
                elif '(' in stack and stack[-1] != '(':
                    return False
                stack.pop()
                
            elif ch == '}':
                if not stack:
                    return False
                elif '{' not in stack:
                    return False
                elif '{' in stack and stack[-1] != '{':
                    return False
                stack.pop()
                
            elif ch == ']':
                if not stack:
                    return False
                elif '[' not in stack:
                    return False
                elif '[' in stack and stack[-1] != '[':
                    return False
                stack.pop()

        if stack:
            return False
        return True
