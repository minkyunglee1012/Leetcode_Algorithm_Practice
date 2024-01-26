class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ""
        for i in range(len(digits)):
            str_num += str(digits[i])
            
        new_num = int(str_num) + 1
        
        new_str = str(new_num)
        new_list = []
        
        for i in range(len(new_str)):
            new_list.append(int(new_str[i]))
        str(new_num).split
        
        return new_list
        