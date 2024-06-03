#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_points = {} #字典
        for i, interval in enumerate(intervals):
            start_points[interval[0]] = i 
            # 將intervals裡的每個[0]值設為key，index設為value
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        # 按照intervals裡的每個[0]值，將intervals排序（因為bisect函數一定要輸入有序陣列）
        
        result = [-1] * len(intervals)

        for i, interval in enumerate(intervals):
            index = bisect_left(sorted_intervals, [interval[1], -float('inf')])
            # 依序找到大於[1]值那個interval的(sorted)index

            if index != len(intervals):
                result[i] = start_points[sorted_intervals[index][0]]
                # 用(sorted)interval的[0]值找回原本的index

        return result
# @lc code=end

