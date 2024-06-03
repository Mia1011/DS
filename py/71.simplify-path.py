#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        name = []
        path = path.split("/")
        for p in path:
            if name and p == "..":
                name.pop()
            elif p not in [".", "", ".."]:
                name.append(p)
                
        return "/" + "/".join(name) 
# @lc code=end

