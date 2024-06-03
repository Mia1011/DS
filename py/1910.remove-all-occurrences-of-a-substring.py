#
# @lc app=leetcode id=1910 lang=python3
#
# [1910] Remove All Occurrences of a Substring
#

# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        test = True
        while test:
            test = False
            i = s.find(part) # 找part出現的位置
            if i != -1: # 如果有找到的話
                s = s[ :i] + s[i+len(part): ]
                test = True
        return s
# @lc code=end

