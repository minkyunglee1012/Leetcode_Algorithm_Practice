class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        cross_num = []
        x_nums = nums[:n]
        y_nums = nums[n:]

        for i in range(len(x_nums)):
            cross_num.append(x_nums[i])
            cross_num.append(y_nums[i])
            
        return cross_num