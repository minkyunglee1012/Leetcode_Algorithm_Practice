class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        bottles = numBottles
        
        if numBottles < numExchange:
            return bottles
        
        while numBottles >= numExchange:
            bottles += numBottles // numExchange
            numBottles = numBottles//numExchange + numBottles%numExchange

            
        return bottles