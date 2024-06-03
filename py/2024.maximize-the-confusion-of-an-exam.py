#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        Tmax = self.solve(answerKey, k, 'T')
        Fmax = self.solve(answerKey, k, 'F')

        return max(Tmax, Fmax)

    def solve(self, answerKey: str, k: int, opt: str) -> int:
        n = len(answerKey)
        size, k2, l = -1, 0, 0  # 最長連續長度,目前改變數量,左極
        for r in range(n):  # 右極先移動
            if answerKey[r] != opt:  # 不一樣就改變
                k2 += 1
            while k2 > k:  # 但如果超過指定改變數量
                if answerKey[l] != opt:  # 左極開始移動，跳過先前的改變，直到數量符合規定
                    k2 -= 1
                l += 1
            size = max(r - l + 1, size)
        return size
    
# @lc code=end

