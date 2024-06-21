class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict_item1 = {}
        dict_item2 = {}
        
        for i in range(len(items1)):
            dict_item1[items1[i][0]] = items1[i][1]
            
        for j in range(len(items2)):
            dict_item2[items2[j][0]] = items2[j][1]
            
        # print(dict_item1)
        # print(dict_item2)

        output = []
        
        for key, val in dict_item1.items():
            # print(key, val)
            if key in dict_item2:
                output.append([key, val + dict_item2[key]])
            else:
                output.append([key, val])

        for key, val in dict_item2.items():
            if key not in dict_item1:
                output.append([key, val])
                
                
        return sorted(output)
                    
        
        