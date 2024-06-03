--
-- @lc app=leetcode id=1667 lang=mysql
--
-- [1667] Fix Names in a Table
--

-- @lc code=start
# Write your MySQL query statement below
SELECT user_id, CONCAT(upper(LEFT(name, 1)), lower(SUBSTR(name, 2))) as name
FROM Users
ORDER BY user_id
-- @lc code=end

