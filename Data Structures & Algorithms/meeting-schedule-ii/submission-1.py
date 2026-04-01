"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque
from heapq import heappop, heappush

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1: return len(intervals)
        intervals = sorted(intervals, key=lambda interval: interval.start)

        curr = 1
        res = 1
        rooms = [intervals[0].end]
        print(intervals)
        for interval in intervals[1:]:
            print(interval, rooms, curr, res)
            if interval.start > rooms[0]:
                heappop(rooms)
                curr -= 1
            else:
                res = max(curr, res)
            curr += 1
            heappush(rooms, interval.end)
            print(interval, rooms, curr, res)

        return max(curr, res)