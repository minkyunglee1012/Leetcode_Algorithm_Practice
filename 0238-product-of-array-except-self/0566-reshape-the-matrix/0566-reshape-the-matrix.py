class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
                return mat
        else:
            reverse = [[0] * c for _ in range(r)]
            
            arr_array = []
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    arr_array.append(mat[i][j])

            for row in range(len(reverse)):
                for col in range(len(reverse[row])):
                    reverse[row][col] = arr_array[0]
                    arr_array.pop(0)
        return reverse