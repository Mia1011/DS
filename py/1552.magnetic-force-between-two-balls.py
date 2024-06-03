#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#

# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def canPlaceBalls(distance):
            count, last_position = 1, position[0]
            for pos in position[1:]:
                if pos - last_position >= distance:
                    count += 1
                    last_position = pos
                    if count == m:
                        return True
            return False
        
        l, r = 1, position[-1] - position[0]  
        while l < r:
            mid = (l + r + 1) // 2
            if canPlaceBalls(mid):
                l = mid
            else:
                r = mid - 1
        return l
    
# @lc code=end

