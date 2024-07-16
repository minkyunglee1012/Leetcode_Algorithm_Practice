class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n = bin(n)[2:]
        # print(n)
        n = n[::-1]
        # print(n)
        
        output = {'even':0, 'odd':0}
        
        for i in range(len(n)):
            if n[i] == '1':
                if i%2 == 0:
                    output['even'] += 1
                else:
                    output['odd'] += 1
            
        return [output['even'], output['odd']]
                