class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        len_pos = {}
        res = 1
        for idx, c in enumerate(s):
            if c not in len_pos:
                len_pos[c] = (1, idx)
            else:
                longest, last_idx = len_pos[c]
                len_pos[c] = (max(longest, idx - last_idx), idx)
            res = max(res, len_pos[c][0])
        print(res, len_pos)
        if len(len_pos) > 1 and all(c==1 for _, (_, c) in len_pos.items()):
            print('if', len(len_pos))
            return len(s)
        return res