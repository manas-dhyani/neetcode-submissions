"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda st : st.start )
        if len(intervals) == 0:
            return True
        lastEnd = intervals[0].end
        for i in intervals:
            if i == intervals[0]:
                continue
            prev = i.start
            if prev < lastEnd:
                return False
            lastEnd = i.end           
        return True    