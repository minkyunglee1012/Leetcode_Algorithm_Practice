class Solution:
    def maximum69Number (self, num: int) -> int:
        if num == 9999:
            return num
        str_num = list(str(num))

        for i in range(len(str_num)):
            if str_num[i] == '9':
                pass
            else:
                str_num[i] = '9'
                break

        str_num = ''.join(str_num)
        return int(str_num)