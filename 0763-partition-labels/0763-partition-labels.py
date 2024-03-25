class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = 1
        count = 0
        answer = []

        while (idx < len(s) + 1):
            count += 1
            # set 메서드 intersetcion
            # set(a).intersection(set(b)) => a와 b의 교집합
            if not(set(s[:idx]).intersection(set(s[idx:]))):
                answer.append(count)
                count = 0
            idx+=1

        return answer