class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        car_points = []
        
        for i in range(len(nums)):
            car_points += [nums[i][0] + n for n in range(nums[i][1]-nums[i][0]+1)]
            
        # print(car_points)
        car_points = list(set(car_points))
        
        return len(car_points)