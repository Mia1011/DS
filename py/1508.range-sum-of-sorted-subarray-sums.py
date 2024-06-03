#
# @lc app=leetcode id=1508 lang=python3
#
# [1508] Range Sum of Sorted Subarray Sums
#

# @lc code=start
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            presum = 0
            for j in range(i, len(nums)):
                presum += nums[j]  # 連續數的總和
                res.append(presum)
        res.sort()
        return sum(res[left-1:right]) % 1_000_000_007
# @lc code=end

