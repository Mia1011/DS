#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        currentRow = 0
        goingDown = False
        
        for char in s:
            rows[currentRow] += char
            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown  # 改變方向
            currentRow += 1 if goingDown else -1

        return ''.join(rows)
    
# @lc code=end

