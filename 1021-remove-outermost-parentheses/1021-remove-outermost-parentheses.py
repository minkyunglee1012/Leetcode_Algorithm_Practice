class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = ""
        stack = []

        a = ""

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                stack.pop()
            a += s[i]

            # 스택이 비어있다면 (완전한 괄호 쌍을 찾은 경우) 
            # a의 가장 바깥쪽 괄호를 제거한 후 output에 추가 후 초기화
            if not stack:
                # print(stack)
                output += a[1:-1]
                a = ""

        return output