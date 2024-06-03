#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1 # 往小的移
            else:
                right = mid # 往小的移
        return nums[left]
# @lc code=end

