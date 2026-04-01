from heapq import heappush

class MedianFinder:

    def __init__(self):
        self.stream = []
        self.length = 0

    def addNum(self, num: int) -> None:
        heappush(self.stream, num)
        self.length += 1

    def findMedian(self) -> float:
        mid = self.length // 2
        if self.length == 1:
            return self.stream[0]
        if self.length % 2 != 0:
            return self.stream[mid]
        return (self.stream[mid - 1] + self.stream[mid]) / 2
