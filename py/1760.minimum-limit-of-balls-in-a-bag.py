#
# @lc app=leetcode id=1760 lang=python3
#
# [1760] Minimum Limit of Balls in a Bag
#

# @lc code=start
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lo, hi = 1, 1_000_000_000
        while lo < hi: 
            mid = lo + hi >> 1
            if sum((x-1)//mid for x in nums) <= maxOperations: 
                hi = mid
            else: 
                lo = mid + 1
        return lo
# @lc code=end

