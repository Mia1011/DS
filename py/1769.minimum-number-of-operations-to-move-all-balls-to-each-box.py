#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        move = []

        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if j != i and boxes[j] == '1': 
                    count = count + abs(i-j)
            move.append(count)
        return move
# @lc code=end

