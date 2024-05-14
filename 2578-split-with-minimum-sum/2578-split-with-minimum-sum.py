class Solution:
    def splitNum(self, num: int) -> int:
        if num < 100:
            # print(sum([int(i) for i in str(num)]))
            return sum([int(i) for i in str(num)])

        num = sorted([i for i in str(num)])
        a, b = "", ""

        for i in range(len(num)):
            if i%2 == 0:
                print(i)
                a += num[i]
            else:
                b += num[i]

        # print(int(a) + int(b))
        return int(a) + int(b)