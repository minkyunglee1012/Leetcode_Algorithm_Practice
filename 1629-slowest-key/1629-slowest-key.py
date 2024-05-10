class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = [releaseTimes[0]]
        for i in range(1, len(releaseTimes)):
            duration.append(releaseTimes[i] - releaseTimes[i-1])

        duration_max = max(duration)
        keypress = []

        while duration_max in duration:
            keypress.append(keysPressed[duration.index(duration_max)])
            duration[duration.index(duration_max)] = 0

        return max(keypress)