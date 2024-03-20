class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        first_reverse = []
        for i in range(len(image)):
            first_reverse.append(image[i][::-1])
            
        for i in range(len(first_reverse)):
            for j in range(len(first_reverse[i])):
                if first_reverse[i][j] == 0:
                    first_reverse[i][j] = 1
                elif first_reverse[i][j] == 1:
                    first_reverse[i][j] = 0
                    
        return first_reverse
