class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        num_list = [str(i) for i in range(left, right+1)]
        print(num_list)
        
        output = []
        
        for i in range(len(num_list)):
            cnt = 0
            for j in range(len(num_list[i])):
                if num_list[i][j] != '0' and int(num_list[i]) % int(num_list[i][j]) == 0:
                    cnt += 1
            if cnt==len(num_list[i]):
                output.append(int(num_list[i]))
                    
        return output