#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]

        for c in candidates:
            for i in range(1, target+1):
                if c > i: continue
                if c == i: 
                    dp[i].append([c])
                else:
                    for r in dp[i-c]:
                        dp[i].append(r+[c])
        return dp[target]        
# @lc code=end

