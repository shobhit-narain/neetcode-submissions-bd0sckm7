'''
    0 1 2 3 4 5 6
    z x y z x y z
   idx c    lens
    0, z -> {z:(1,0)}
    1, x -> {z:(1,0), x:(1,1)}
    2, y -> {z:(1,0), x:(1,1), y:(1,2)}
    3, z -> {z:(1,0), x:(1,1), y:(1,2)} | z: (max(lens[c][0], idx-lens[c][1]), idx)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_pos = {}
        res = 1
        for idx, c in enumerate(s):
            if c not in len_pos:
                len_pos[c] = (1, idx)
            else:
                longest, last_idx = len_pos[c]
                len_pos[c] = (max(longest, idx - last_idx), idx)
            res = max(res, len_pos[c][0])

        return res