from collections import defaultdict
import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words or beginWord == endWord:
            return 0

        adj_list = defaultdict(list)
        n = len(wordList[0])
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + '.' + word[i+1:]
                adj_list[pattern].append(word)

        q = deque([[beginWord]])
        visited = set([beginWord])
        lev = 0
        while q:
            lev += 1
            nodes = q.popleft()
            nxt_level = []
            for node in nodes:
                if node == endWord:
                    return lev
                for i in range(n):
                    pat = node[:i] + '.' + node[i+1:]
                    for ngbr in adj_list[pat]:
                        if ngbr not in visited:
                            visited.add(ngbr)
                            nxt_level.append(ngbr)
            if nxt_level:
                q.append(nxt_level)

        return res
