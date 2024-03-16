class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = {}

        for i, v in enumerate(s):
            if v in my_dict:
                my_dict[v] += 1
            else:
                my_dict[v] = 1

        my_dict

        sorted_values = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        answer = ''
        for key, value in sorted_values:
            answer += key* value

        return answer