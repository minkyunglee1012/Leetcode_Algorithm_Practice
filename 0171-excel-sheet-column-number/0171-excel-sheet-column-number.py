class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        column_num = 0
        columnTitle = columnTitle[::-1]
        for i in range(len(columnTitle)):
            column_num += (digits.index(columnTitle[i]) + 1) * (26 ** i)
            
        return column_num