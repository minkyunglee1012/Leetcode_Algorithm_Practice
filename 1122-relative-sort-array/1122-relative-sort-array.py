class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        also = {}
        not_appear = []
        
        for i in arr1:
            if i in arr2:
                if i not in also:
                    also[i] = 1
                else:
                    also[i] += 1
            else:
                not_appear.append(i)
        
        not_appear = sorted(not_appear)
                
        # print(also)
                    
        
        result = []
        for i in arr2:
            for j in range(also[i]):
                result += [i]
                
        return result + not_appear
                
        