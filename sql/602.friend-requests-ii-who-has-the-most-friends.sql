--
-- @lc app=leetcode id=602 lang=mysql
--
-- [602] Friend Requests II: Who Has the Most Friends
--

-- @lc code=start
# Write your MySQL query statement below
SELECT id, count(id) as num
FROM (
    (
    SELECT requester_id as id
    FROM RequestAccepted
    )
    UNION ALL
    (
    SELECT accepter_id as id
    FROM RequestAccepted
    )
) t2
GROUP BY id
ORDER BY count(id) DESC
LIMIT 1
-- @lc code=end

