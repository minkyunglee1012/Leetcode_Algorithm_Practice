class Solution:
    def judgeCircle(self, moves: str) -> bool:
        def move(s, i, j):
            if s=='L':
                j -= 1
            elif s=='R':
                j += 1
            elif s=='U':
                i += 1
            elif s=='D':
                i -= 1
            return i, j
        i, j =0, 0
        for s in moves:
            i, j = move(s, i, j)

        return i==0 and j ==0

