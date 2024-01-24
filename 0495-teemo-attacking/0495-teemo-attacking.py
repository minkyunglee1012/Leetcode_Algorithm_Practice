class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        attack_time = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i + 1] - timeSeries[i] > duration:
                attack_time += duration
            else:
                attack_time += timeSeries[i + 1] - timeSeries[i]
        return attack_time + duration