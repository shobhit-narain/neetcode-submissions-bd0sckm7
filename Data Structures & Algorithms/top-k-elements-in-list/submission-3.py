import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        for num, f in freq.items():
            heapq.heappush(most_freq, (f, num))
            if len(most_freq) > k:
                heapq.heappop(most_freq)
        return [v for _, v in most_freq]
