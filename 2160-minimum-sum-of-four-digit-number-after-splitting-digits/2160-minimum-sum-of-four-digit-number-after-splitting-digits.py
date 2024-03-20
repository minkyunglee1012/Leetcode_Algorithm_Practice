class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        num_list = []
        for i in range(len(num)):
            num_list.append(num[i])
            
        num_list.sort()
        
        return int(str(num_list[0]) + str(num_list[2])) + int(str(num_list[1]) + str(num_list[3]))
        
