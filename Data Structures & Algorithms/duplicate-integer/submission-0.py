class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            b = len(a)
            a.add(i)
            c = len(a)
            if b == c:
                return True
        return False
        