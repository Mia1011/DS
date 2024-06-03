--
-- @lc app=leetcode id=1731 lang=mysql
--
-- [1731] The Number of Employees Which Report to Each Employee
--

-- @lc code=start
# Write your MySQL query statement below
SELECT b.employee_id, b.name, 
    count(a.reports_to) as reports_count, 
    round(avg(a.age)) as average_age
FROM Employees a
JOIN Employees b ON a.reports_to = b.employee_id
GROUP BY b.employee_id
ORDER BY b.employee_id

# 用 inner join
# a表格保留非null的reports_to和age，b表格保留對應的id和name
-- @lc code=end

