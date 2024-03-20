class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sort_arr = sorted(arr)
        sort_arr_2 = sorted(arr)[::-1]

        check = []
        for i in range(1, len(sort_arr)):

            if sort_arr[i] - sort_arr[i-1] != sort_arr[1] - sort_arr[0]:
                    check.append(False)

        for i in range(1, len(sort_arr_2)):

            if sort_arr_2[i] - sort_arr_2[i-1] != sort_arr_2[1] - sort_arr_2[0]:
                    check.append(False)

        if not check:
            return True
        else:
              return False
