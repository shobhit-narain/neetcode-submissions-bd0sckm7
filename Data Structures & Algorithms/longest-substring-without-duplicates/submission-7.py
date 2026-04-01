class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        l, res = 0, 0
        for r, c in enumerate(s):
            while c in curr:
                curr.remove(s[l])
                l += 1
            curr.add(c)
            res = max(res, r-l+1)
        return res