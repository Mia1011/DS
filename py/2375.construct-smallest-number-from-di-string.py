#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#

# @lc code=start
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern += 'I'
        res = s = ''
        for i,p in enumerate(pattern):
            s += str(i+1)
            if p == 'I':
                res += s[::-1]
                s =''
        return res
# @lc code=end

