#
# @lc app=leetcode id=2498 lang=python3
#
# [2498] Frog Jump II
#

# @lc code=start
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ans = stones[1]
        for i in range(2, len(stones)): 
            ans = max(ans, stones[i] - stones[i-2])
        return ans 
# @lc code=end

