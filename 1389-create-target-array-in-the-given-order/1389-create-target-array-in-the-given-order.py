class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [nums[index[0]]]
        
        # 전 인덱스가 다음 인덱스보다 크거나 같으면
        # 리스트 i부터 슬라이싱으로 나눠서 num[i] 붙여주고 그 뒤 다시 붙이자.
        for i in range(1, len(nums)):
            work = target[index[i]:]
            target = target[:index[i]] + [nums[i]] + work
            
        return target
            