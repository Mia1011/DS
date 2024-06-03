--
-- @lc app=leetcode id=180 lang=mysql
--
-- [180] Consecutive Numbers
--

-- @lc code=start
# Write your MySQL query statement below
SELECT distinct num AS ConsecutiveNums
FROM (
    SELECT num,
        lead(num, 1) over(order by id) AS num1, 
        lead(num, 2) over(order by id) AS num2
    FROM logs
) AS logs2
WHERE (num=num1) and (num1=num2)
-- @lc code=end

