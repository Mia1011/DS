#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tail[m] < x:
                    i = m + 1
                else:
                    j = m
            tail[i] = x
            size = max(i + 1, size)
        return size
# @lc code=end

