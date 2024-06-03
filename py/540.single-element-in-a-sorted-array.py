#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = 2 * ((left + right) // 4)  # 一定是偶數index
            if nums[mid] == nums[mid+1]:
                left = mid+2  # [mid]和[mid+1]前都是成雙的
            else:
                right = mid  # [mid]或之前有落單的
        return nums[left]        
# @lc code=end

