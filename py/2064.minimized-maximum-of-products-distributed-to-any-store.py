#
# @lc app=leetcode id=2064 lang=python3
#
# [2064] Minimized Maximum of Products Distributed to Any Store
#

# @lc code=start
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo, hi = 1, max(quantities)
        while lo < hi: 
            mid = lo + hi >> 1
            if sum(ceil(qty/mid) for qty in quantities) <= n: hi = mid 
            else: lo = mid + 1
        return lo
# @lc code=end

