class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fB_list = []
        for i in range(n):
            if (i + 1) % 15 == 0:
                fB_list.append('FizzBuzz')
            
            elif (i + 1) % 3 == 0:
                fB_list.append('Fizz')
                
            elif (i + 1) % 5 == 0:
                fB_list.append('Buzz')
                
            else:
                fB_list.append(str(i+1))
                
        return fB_list
                
        