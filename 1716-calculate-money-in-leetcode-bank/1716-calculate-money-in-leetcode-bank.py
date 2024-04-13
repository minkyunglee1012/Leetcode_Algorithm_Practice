class Solution:
    def totalMoney(self, n: int) -> int:
        day = 0
        money = 0
        lot = 0
        while day < n:
            if day%7 == 0:
                lot = day//7 + 1
            else:
                lot += 1
                
            money += lot
            day += 1

        return money