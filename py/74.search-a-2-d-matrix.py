#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix: # 一個一個row檢查
            if row[-1] >= target: # 有可能在那個row
                if target in row:
                    return True
        return False
# @lc code=end

