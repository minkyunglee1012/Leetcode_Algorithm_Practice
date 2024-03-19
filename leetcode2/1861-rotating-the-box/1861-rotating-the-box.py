class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            row = len(box[i]) - 1
            for j in range(row, -1, -1):
                if box[i][j] == '*':
                    row = j-1

                elif box[i][j] == '#':
                    box[i][row], box[i][j] = box[i][j], box[i][row]
                    row -= 1

        import numpy as np
        return list(np.transpose(box[::-1]))