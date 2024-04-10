class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []

        for i in range(len(queries)):
            cnt = 0
            for j in range(len(points)):
                if ((queries[i][0] - points[j][0]) ** 2 + (queries[i][1] - points[j][1]) ** 2) ** (1/2) <= queries[i][2]:
                    cnt += 1
            result.append(cnt)


        return result