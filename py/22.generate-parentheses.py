#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        result = []
        self.parentheses(n, n, "", result)
        return result

    def parentheses(self, l, r, item, result):
        if l > r:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.parentheses(l-1, r, item + "(", result)
        if r > 0:
            self.parentheses(l, r-1, item + ")", result)        
# @lc code=end

