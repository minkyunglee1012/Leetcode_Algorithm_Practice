class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        freq = nums[::2]
        val = nums[1::2]
        
        for i in range(len(freq)):
            result += [val[i]] * freq[i]
            
        return result
