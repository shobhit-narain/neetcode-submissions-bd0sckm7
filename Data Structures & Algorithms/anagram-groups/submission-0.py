from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = defaultdict(list)
        for s in strs:
            l, ltrs = len(s), set(s)
            sets[f"{l}_{ltrs}"].append(s)
            print(sets)
        return [l for _, l in sets.items()]