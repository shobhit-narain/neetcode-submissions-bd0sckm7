class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for idx, num in enumerate(nums):
            if num not in idxs:
                idxs[num] = idx
        for num in nums:
            if target - num in idxs:
                return [idxs[num], idxs[target-num]]
        return []
        