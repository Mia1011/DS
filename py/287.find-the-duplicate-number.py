#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # return mode(a) :)
        
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r+l) // 2  # 取一個參考值（中位數/平均數）
            if sum(v <= m for v in nums) - m > 0:  # 如果(小於參考值)數量超過目前陣列長度的一半
                result = m  # 代表重複項在(小於參考值)這個範圍
                r = m - 1  # 限縮陣列，使參考值變小
            else:
                l = m + 1
        return result
        # 陣列長度和數值大小可以相互轉換，所以程式碼會有點難理解目前是指哪個，有點抽象。

# @lc code=end

