--
-- @lc app=leetcode id=1934 lang=mysql
--
-- [1934] Confirmation Rate
--

-- @lc code=start
# Write your MySQL query statement below
SELECT s.user_id, round(avg(if(c.action = "confirmed", 1, 0)), 2) confirmation_rate
FROM Confirmations c
RIGHT JOIN Signups s ON c.user_id = s.user_id
GROUP BY user_id
-- @lc code=end

