--
-- @lc app=leetcode id=610 lang=mysql
--
-- [610] Triangle Judgement
--

-- @lc code=start
# Write your MySQL query statement below
SELECT x, y, z,  # 也可以用*代替
    IF(x+y>z and y+z>x and z+x>y, "Yes", "No") AS triangle
FROM Triangle
-- @lc code=end

