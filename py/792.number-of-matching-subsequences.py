#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def sub(st):
            pos = -1
            for char in st:
                pos = s.find(char, pos + 1)
                if pos == -1: return False
            return True
        return sum(map(sub, words))
# @lc code=end

