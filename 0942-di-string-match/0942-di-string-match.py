class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = 0
        end = len(s)
        output = []
        perm = [j for j in range(start, end+1)]
        for i in range(len(s)):
            if s[i] == "I":
                output.append(perm[start])
                start += 1
            elif s[i] == "D":
                output.append(perm[end])
                end -= 1

        output.append(perm[start])
        return output
