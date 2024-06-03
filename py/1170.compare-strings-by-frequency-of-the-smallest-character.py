#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#

# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            t = sorted(list(s))[0]
            return s.count(t)
        
        query = [f(x) for x in queries]
        word = [f(x) for x in words]
        ans = []

        for x in query:
            count = 0
            for y in word:
                if y > x:
                    count += 1
            ans.append(count)
        return ans
    
# @lc code=end

