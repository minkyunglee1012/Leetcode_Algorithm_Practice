class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = (s1+' '+s2).split(' ')
        dict = {}
        for idx, val in enumerate(s):
            if val not in dict:
                dict[val] = 0
                dict[val] += 1
            else:
                dict[val] += 1
        # print(dict)
        # print(dict.keys())
        output = []
        for key in dict.keys():
            if dict[key] == 1:
                output.append(key)

        return output