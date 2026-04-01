import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        print(freq)
        for f, num in freq.items():
            heapq.heappush(most_freq, (-1 * f, num))
            print(most_freq)
        return [v for _, v in most_freq[:k]]
