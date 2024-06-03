#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        
        maxLen = 1
        maxStr = s[0]
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if j-i+1 > maxLen and s[i:j+1] == s[i:j+1][::-1]:
                    maxLen = j - i + 1
                    maxStr = s[i:j+1]

        return maxStr
# @lc code=end

