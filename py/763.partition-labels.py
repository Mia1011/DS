#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        L = len(s)
        last = {s[i]: i for i in range(L)} # 字母對應最後出現的位置
        i, ans = 0, []
        while i < L:
            end, j = last[s[i]], i + 1
            while j < end: # 檢查i~end
                if last[s[j]] > end:
                    end = last[s[j]]
                j += 1
           
            ans.append(end - i + 1)
            i = end + 1           
        return ans        
# @lc code=end

