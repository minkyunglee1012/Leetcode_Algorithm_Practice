class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x_list = [int(str(x)[i]) for i in range(len(str(x)))]
        if x%sum(x_list) == 0:
            # print(sum(x_list))
            return sum(x_list)
        else:
            # print(-1)
            return -1