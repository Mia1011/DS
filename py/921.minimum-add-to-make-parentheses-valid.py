#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    count += 1
                else:
                    stack.pop()
        return count + len(stack)
# @lc code=end

