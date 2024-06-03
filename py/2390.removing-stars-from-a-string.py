#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        new_s = ''
        for i in range(len(s)):
            if s[i] == '*':
                new_s = new_s[ :len(new_s)-1]
            else:
                new_s = new_s + s[i]
        return new_s
# @lc code=end

