class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
        return [min(i,j)+1, max(i,j)+1]