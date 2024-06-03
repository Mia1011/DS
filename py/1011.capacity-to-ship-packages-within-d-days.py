#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        # 定義需要多少天運送
        def shipDays(ShipCapacity: int) -> int:
            days = 1
            capacity = 0
            for weight in weights:
                if capacity + weight > ShipCapacity:
                    days += 1
                    capacity = weight
                else:
                    capacity += weight
            return days

        while left < right:
            mid = (left + right) // 2
            if shipDays(mid) <= days:
                right = mid
            else:
                left = mid + 1
        return left
    
# @lc code=end

