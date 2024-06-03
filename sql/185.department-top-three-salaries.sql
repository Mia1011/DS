--
-- @lc app=leetcode id=185 lang=mysql
--
-- [185] Department Top Three Salaries
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
    SELECT d.name Department, e.name Employee, e.salary Salary, 
    DENSE_RANK() OVER (
        PARTITION BY departmentId
        ORDER BY salary DESC
    ) top_salary
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) t2
WHERE top_salary in (1, 2, 3)
-- @lc code=end

