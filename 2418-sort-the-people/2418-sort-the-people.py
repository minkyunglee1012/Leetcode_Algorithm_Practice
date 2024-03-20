class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sort_names = []
        for i in range(len(heights)):
            a = heights.index(max(heights))
            sort_names.append(names[a])
            del heights[a]
            del names[a]


        return sort_names
