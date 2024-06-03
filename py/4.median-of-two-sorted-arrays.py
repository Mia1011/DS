#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)

        if length % 2 == 1: #奇數個
            return float(merged[length//2]) #求整數，不考慮餘數
        else:
            return float((merged[length//2-1] + merged[length//2]) / 2.0) #2.0!
# @lc code=end
