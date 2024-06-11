class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        encrypted = []

        for i in range(len(nums)):
            encrypted.append(int(max([i for i in str(nums[i])]) * len(str(nums[i]))))

        return sum(encrypted)