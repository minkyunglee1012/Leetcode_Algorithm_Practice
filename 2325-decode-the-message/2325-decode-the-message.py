class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        # 먼저 key 문자열을 띄어쓰기를 제외하고 합한 후
        # 중복 값을 제거해 주자
        new_key = ''
        for i in range(len(key)):
            if key[i] == ' ':
                pass
            elif key[i] not in new_key:
                new_key += key[i]
                
        # message 순회하면서 ' '면 그대로 더하고
        # 문자열은 new_key의 인덱스를 digits에 넣어서 구하자
        digits = 'abcdefghijklmnopqrstuvwxyz'
        answer = ''
        for ms in message:
            if ms == ' ':
                answer += ' '
            else:
                answer += digits[new_key.index(ms)]
                
        return answer
        