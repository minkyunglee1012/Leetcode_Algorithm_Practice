from collections import deque

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        queue = deque(range(len(tickets)))
        sec = 0

        while tickets[k] != 0:
            index = queue.popleft()
            if tickets[index] != 0:
                tickets[index] = tickets[index] - 1
                sec += 1
            queue.append(index)

        return sec
        
