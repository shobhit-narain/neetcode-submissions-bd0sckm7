class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [1] * n, [1] * n
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
            r[-i-1] = r[-i] * nums[-i]
        return [l[i] * r[i] for i in range(n)] 