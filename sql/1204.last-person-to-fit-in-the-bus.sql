--
-- @lc app=leetcode id=1204 lang=mysql
--
-- [1204] Last Person to Fit in the Bus
--

-- @lc code=start
# Write your MySQL query statement below
SELECT q1.person_name
FROM Queue q1
JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.person_id
HAVING sum(q2.weight) <= 1000
ORDER BY sum(q2.weight) DESC
LIMIT 1
-- @lc code=end

