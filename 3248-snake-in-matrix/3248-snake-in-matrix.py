class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        matrix = []
        count = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(count)
                count += 1
            matrix.append(row)
        
        dictation = [0, 0]
        for i in range(len(commands)):
            if commands[i] == 'RIGHT':
                dictation[1] += 1
            if commands[i] == 'LEFT':
                dictation[1] -= 1
            if commands[i] == 'UP':
                dictation[0] -= 1
            if commands[i] == 'DOWN':
                dictation[0] += 1
                
        return matrix[dictation[0]][dictation[1]]