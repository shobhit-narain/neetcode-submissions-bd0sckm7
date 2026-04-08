/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        map<int, int> timeline;
        for (const auto& interval: intervals) {
            timeline[interval.start]++;
            timeline[interval.end]--;
        }
        int res = 0, rooms = 0;
        for (const auto& [t, ev] : timeline) {
            rooms += ev;
            res = max(res, rooms);
        }
        return rooms;
    }
};
