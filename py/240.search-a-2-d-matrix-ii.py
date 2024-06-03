#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0: # 從右上角開始
            if target < matrix[i][j]: # 目標較小就往左移
                j -= 1
            elif target > matrix[i][j]: # 目標較大就往下移
                i += 1
            else:
                return True
        return False
# @lc code=end

