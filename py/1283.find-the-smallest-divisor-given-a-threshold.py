#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            sum = 0
            for n in nums:
                sum += math.ceil(n/mid)
            if sum <= threshold:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
            print(mid, start, end)
        return ans
# @lc code=end

