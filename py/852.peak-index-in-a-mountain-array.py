#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1

        while(left <= right):
            mid = (left + right) // 2
            if arr[mid-1] <= arr[mid] and arr[mid+1] <= arr[mid]:
                return mid
            elif arr[mid-1] > arr[mid]:
                right = mid
            else:
                left = mid
# @lc code=end

