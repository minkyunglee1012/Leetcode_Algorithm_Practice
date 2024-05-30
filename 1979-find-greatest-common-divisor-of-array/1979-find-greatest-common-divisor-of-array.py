class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest_num = min(nums)
        largest_num = max(nums)

        smallest_gcd = []

        for i in range(1, smallest_num+1):
            if smallest_num % i == 0:
                smallest_gcd.append(i)

        smallest_gcd = sorted(smallest_gcd)[::-1]

        for n in range(len(smallest_gcd)):
            if largest_num % smallest_gcd[n] == 0:
                return smallest_gcd[n]
            