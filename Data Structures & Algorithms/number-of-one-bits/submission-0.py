class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0 + n % 2
        for i in range(31):
            n = n >> 1
            sum += n % 2
        return sum