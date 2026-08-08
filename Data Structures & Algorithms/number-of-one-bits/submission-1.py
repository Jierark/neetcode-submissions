class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        for i in range(32):
            mask = (1 << i)
            if (n & mask):
                sum += 1
        return sum
        