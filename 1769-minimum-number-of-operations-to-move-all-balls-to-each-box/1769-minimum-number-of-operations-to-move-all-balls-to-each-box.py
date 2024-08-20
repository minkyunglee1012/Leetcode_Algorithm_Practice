class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        output = [0] * len(boxes)
        count = op = 0
        
        for i in range(len(boxes)):
            output[i] = op
            count += boxes[i] == '1'
            op += count
        op = count = 0
        
        for i in range(len(boxes)-1, -1, -1):
            output[i] += op
            count += boxes[i] == '1'
            op += count
        
        return output
