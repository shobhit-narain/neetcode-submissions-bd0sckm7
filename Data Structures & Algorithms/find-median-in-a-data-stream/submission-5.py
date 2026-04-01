
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        self.lens = [0, 0]

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
            self.lens[1] += 1
        else:
            heapq.heappush(self.small, -1 * num)
            self.lens[0] += 1

        if len(self.large) > len(self.small) + 1:
            elem = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * elem)
            self.lens = [self.lens[0] + 1, self.lens[1] - 1]
        elif len(self.small) > len(self.large) + 1:
            elem = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, elem)
            self.lens = [self.lens[0] - 1, self.lens[1] + 1]

    def findMedian(self) -> float:
        if self.lens[0] > self.lens[1]:
            return -1 * self.small[0]
        elif self.lens[1] > self.lens[0]:
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
