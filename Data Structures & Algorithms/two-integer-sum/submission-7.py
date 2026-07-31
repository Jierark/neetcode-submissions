class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []
        for i, j in enumerate(nums):
            sorted_nums.append([j,i]) # elm 0 is number, elm 1 is original index
        sorted_nums.sort()
        left = 0
        right = len(sorted_nums)-1
        print(left, right)
        while left < right:
            cur = sorted_nums[left][0] + sorted_nums[right][0]
            if cur < target:
                left += 1
            elif cur > target:
                right -= 1
            else:
                return [min(sorted_nums[left][1], sorted_nums[right][1]),max(sorted_nums[left][1], sorted_nums[right][1])]
        return []