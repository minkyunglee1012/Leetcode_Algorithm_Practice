class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds_ = 0
        for i in arr:
            if i & 1 == 1:
                odds_ += 1
                if odds_ == 3:
                    return True
            else:
                odds_ = 0
        return False
        
