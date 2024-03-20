class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i+1 for i in range(n)]
        # circle

        if k == 1:
            print(circle[-1])

        while len(circle) > 1:
            if k == 2:
                first = circle.pop(0)
                circle.pop(0)
                circle.append(first)
            else:
                for i in range(k-1):
                    circle.append(circle.pop(0))
                circle.pop(0)
        return circle[0]
