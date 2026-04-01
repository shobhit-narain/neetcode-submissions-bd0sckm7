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

        rooms = [intervals[0].end]
        for interval in intervals[1:]:
            if rooms and rooms[0] <= interval.start:
                heappop(rooms)
            heappush(rooms, interval.end)

        return len(rooms)