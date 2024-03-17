class Solution:
    def rotateTheBox(self, b: List[List[str]]) -> List[List[str]]:
        n=len(b)
        m=len(b[0])
        for i in range(n):
            r=m-1
            for j in range(m-1,-1,-1):
                if b[i][j]=="*":
                    r=j-1
                elif b[i][j]=="#":
                    b[i][r],b[i][j]=b[i][j],b[i][r]
                    r-=1
                    
        return [i[::-1] for i in zip(*b)]