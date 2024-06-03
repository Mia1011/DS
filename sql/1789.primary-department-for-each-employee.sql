--
-- @lc app=leetcode id=1789 lang=mysql
--
-- [1789] Primary Department for Each Employee
--

-- @lc code=start
# Write your MySQL query statement below
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = "Y"

UNION  # 合併查詢到不同列的結果

SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING count(employee_id) = 1
-- @lc code=end

