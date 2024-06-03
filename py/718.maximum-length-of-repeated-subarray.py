#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1  # 總數是存在[+1]的位置

        return max(map(max, dp))        
# @lc code=end

