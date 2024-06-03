#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        s2 = ""
        for i in range(1, n):
            count = 0
            curr = s[0]
            for c in s:
                if c == curr:
                    count += 1
                else:
                    s2 += str(count) + curr
                    count = 1
                    curr = c
            s2 += str(count) + curr
            print(s2)
            s = s2
            s2 = ""
        return s
# @lc code=end

