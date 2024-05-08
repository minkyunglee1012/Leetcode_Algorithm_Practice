class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score)[::-1]
        answer = []
        for i in range(len(score)):
            if sorted_score.index(score[i]) == 0:
                answer.append("Gold Medal")
            elif sorted_score.index(score[i]) == 1:
                answer.append("Silver Medal")
            elif sorted_score.index(score[i]) == 2:
                answer.append("Bronze Medal")
            else:
                answer.append(f"{sorted_score.index(score[i])+1}")
        return answer