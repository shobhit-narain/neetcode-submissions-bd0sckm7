'''
    A A A B A B B
    0 1 2 3 4 5 6

    l   r   seq     most_freq   freq_map        (seq - most_freq) <= k     next_step    ans
    0   1   2       A           {A: 2}          true (0 <= 1)               r += 1      2
    0   2   3       A           {A: 3}          true (0 <= 1)               r += 1      3
    0   3   4       A           {A: 3, B: 1}    true (1 <= 1)               r += 1      4
    0   4   5       A           {A: 4, B: 1}    true (1 <= 1)               r += 1      5   
    0   5   6       A           {A: 4, B: 2}    false(2 > 1)                l += 1      5 (decrease A count)
    1   5   5       A           {A: 3, B: 2}    false (2> 1)                l += 1      5 (decrease A count)
    2   5   4       A           {A: 2, B: 2}    false  (2> 1)               l += 1      5 (decrease A count)
    3   5   3       B           {A: 1, B: }            
'''

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1: return 1
        if k == len(s): return k

        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while ((r - l + 1) - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res