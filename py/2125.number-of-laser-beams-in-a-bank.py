#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#

# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        pre_count = 0
        for i in bank:
            count = i.count('1')
            if count:
                ans += pre_count * count
                pre_count = count
        return ans
# @lc code=end

