#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class MyCalendar:

    def __init__(self):
        self.eventDates = []

    def book(self, start: int, end: int) -> bool:
        for laststart, lastend in self.eventDates:
            if laststart < end and start < lastend:  # 有重疊
                return False
        self.eventDates.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

