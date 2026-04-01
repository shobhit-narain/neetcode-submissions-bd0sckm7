class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    # --- 4 # c o d e 3 # h e y
    # --- 0 1 2 3 4 5 6 7 8 9 10
    def decode(self, s: str) -> List[str]:
        if not s: return []
        res = []
        l = ''
        i = 0
        while i < len(s):
            if s[i] == '#':
                i += 1
                ln = int(l)
                res.append(s[i:i+ln])
                i += ln
                l = ''
            else:
                l += s[i]
                i += 1
        return res        
