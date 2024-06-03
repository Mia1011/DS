#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()        
        prefix = ''
        res = []
        i = 0
        for c in searchWord:
            prefix += c
            i = bisect_left(products, prefix, i)
            res.append([w for w in products[i:i+3] if w.startswith(prefix)])        
        return res  
# @lc code=end

