class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0:
                        return True
                    continue

            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0:
                        return True
                    continue


            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True
                continue
        return False
