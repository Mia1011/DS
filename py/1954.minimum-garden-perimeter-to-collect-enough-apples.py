#
# @lc app=leetcode id=1954 lang=python3
#
# [1954] Minimum Garden Perimeter to Collect Enough Apples
#

# @lc code=start
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left = 1
        right = neededApples
        while left <= right:
            mid = left + (right-left)//2
            max_apple = 2 * mid * (mid + 1) * (2*mid + 1)
            if neededApples <= max_apple:
                right = mid - 1
            else:
                left = mid +1
        return (right + 1) * 8
# @lc code=end

