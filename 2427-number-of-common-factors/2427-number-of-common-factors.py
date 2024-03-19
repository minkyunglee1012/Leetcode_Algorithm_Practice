class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a_gcd = []
        b_gcd = []

        n = 1
        while a >= n:
            if a%n == 0:
                a_gcd.append(n)
            n += 1

        m = 1
        while b >= m:
            if b%m == 0:
                b_gcd.append(m)
            m += 1



        return len(set(a_gcd).intersection(set(b_gcd)))