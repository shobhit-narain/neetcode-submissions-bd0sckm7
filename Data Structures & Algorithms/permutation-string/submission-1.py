class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        # if len(s1) == len(s2): return set(s1) == set(s2)
        n = len(s1)
        freq = {}
        for s in s1:
            if s not in freq:
                freq[s] = 0
            freq[s] += 1
        
        curr = {}
        for i in range(n):
            if s2[i] not in curr:
                curr[s2[i]] = 0
            curr[s2[i]] += 1

        print(freq, curr)
        for i in range(1, len(s2)-n+1):
            print(s2[i-1], s2[i], curr, s2[i+n-1])
            if curr == freq:
                return True
            curr[s2[i-1]] -= 1
            if curr[s2[i-1]] == 0: del curr[s2[i-1]]
            # if s2[i] not in curr:
            #     curr[s2[i]] = 0
            # curr[s2[i]] += 1
            if s2[i+n-1] not in curr:
                curr[s2[i+n-1]] = 0
            curr[s2[i+n-1]] += 1
            print(curr)

        return curr == freq                
