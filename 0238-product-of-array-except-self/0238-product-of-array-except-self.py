class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 1:
            mul = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    mul *= nums[i]

            answer = [0]*len(nums)
            answer[nums.index(0)] = mul
            
            return answer

        elif nums.count(0) >= 2:
            answer = [0] * len(nums)
            
            return answer

        else:
            answer = []
            mul = 1
            for i in range(len(nums)):
                mul *= nums[i]

            for i in range(len(nums)):
                answer.append(int(mul / nums[i]))


        return answer
