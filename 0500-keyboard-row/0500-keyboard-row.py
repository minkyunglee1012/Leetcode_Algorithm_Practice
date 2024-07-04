class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        first_row = list("qwertyuiop")
        second_row = list("asdfghjkl")
        third_row = list("zxcvbnm")
        
        def check(word, keyboard_row):
            return all(i in keyboard_row for i in word.lower())
        
        output = []
        
        for word in words:
            if check(word, first_row) or check(word, second_row) or check(word, third_row)==True:
                output.append(word)
                
        return output

        
        
        
