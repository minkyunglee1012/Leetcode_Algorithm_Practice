class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict = {}
        for idx, val in enumerate(arr):
            if val not in dict:
                dict[val] = 1
            else:
                dict[val] += 1

        output_list = []
        for key in dict.keys():
            if dict[key] == 1:
                output_list.append(key)

        if len(output_list) < k:
            # print("")
            return ""
        else: return output_list[k-1]