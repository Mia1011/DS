--
-- @lc app=leetcode id=577 lang=mysql
--
-- [577] Employee Bonus
--

-- @lc code=start
# Write your MySQL query statement below
SELECT E.name, B.bonus
FROM Employee E
LEFT JOIN Bonus B ON E.empID = B.empId
WHERE B.bonus < 1000 OR B.bonus IS NULL
-- @lc code=end

