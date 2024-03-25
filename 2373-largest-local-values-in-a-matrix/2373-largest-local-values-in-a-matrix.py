class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [[]*(len(grid)-2)]*(len(grid)-2)
        
        length = (len(grid)-2)

        new_list = []


        for i in range(length):
            for j in range(length):
                new_list.append(grid[i][j:j+3])
                new_list.append(grid[i+1][j:j+3])
                new_list.append(grid[i+2][j:j+3])

        a = []


        for i in range(0, len(new_list), 3):
            a.append((max(max(new_list[i]), max(new_list[i+1]), max(new_list[i+2]))))
            # for j in range(len(result)):
            #     for k in range(len(result[j])):
            #         result[j][k] = max(max(new_list[i]), max(new_list[i+1]), max(new_list[i+2]))


        for i in range(len(result)):
            result[i] = a[i*len(result):i*len(result)+len(result)]

        return result