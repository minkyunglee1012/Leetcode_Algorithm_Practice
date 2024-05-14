class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        # 전체 합이 홀수 -> 두 개의 부분집합으로 나눌 수 x
        if total % 2 == 1:
            return False
        
        target = total // 2
        dp = [False]*(target+1)
        dp[0] = True  # 합 0을 만드는 것은 언제나 가능하므로
        
        # 모든 숫자에 대해 반복
        for i in range(len(nums)):
            # 현재 숫자를 사용하여 만들 수 있는 합을 역순으로 검토
            for j in range(target, nums[i]-1, -1):
                # 이전에 j-nums[i] 합을 만들 수 있는 경우, 현재 num 추가하여 j 합도 True
                if dp[j-nums[i]]:
                    dp[j] = True
        
        # target 만들 수 있으면 True 반환
        return dp[target]