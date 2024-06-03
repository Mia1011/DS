#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        count, seen = 0, set()
        for letter in s:
            if letter in seen:
                count += 1
                seen = set(letter)
            else:
                seen.add(letter)
        return count + 1
# @lc code=end

