#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#

# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = defaultdict(list)
        res = []
        for i, v in enumerate(pattern):
            p[v].append(i)
        for word in words:
            w = defaultdict(list)
            for i, v in enumerate(word):
                w[v].append(i)
            if list(w.values()) == list(p.values()):
                res.append(word)
        return res
# @lc code=end

