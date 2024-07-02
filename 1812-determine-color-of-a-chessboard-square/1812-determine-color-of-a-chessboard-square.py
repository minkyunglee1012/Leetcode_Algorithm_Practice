class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        string = 'abcdefgh'
        number = '12345678'
        
        if int(string.index(coordinates[0]) + 1) % 2 == 1:
            if int(number.index(coordinates[1]) + 1) % 2 == 0:
                return True
            return False
        else:
            if int(number.index(coordinates[1]) + 1) % 2 == 1:
                return True
            return False