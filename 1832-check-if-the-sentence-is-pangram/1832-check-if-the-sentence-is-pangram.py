class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = 'abcdefghijklmnopqrstuvwxyz'
        
        # pangram 순회하면서 sentence에 없으면 바로 False return
        for i in range(len(pangram)):
            if pangram[i] not in sentence:
                return False
            
            
            
        return True