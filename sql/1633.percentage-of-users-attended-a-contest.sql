--
-- @lc app=leetcode id=1633 lang=mysql
--
-- [1633] Percentage of Users Attended a Contest
--

-- @lc code=start
# Write your MySQL query statement below
SELECT contest_id, round(count(distinct user_id) / (SELECT count(user_id) FROM Users), 4)*100 percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id

# distict
-- @lc code=end

