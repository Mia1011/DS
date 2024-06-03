--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--

-- @lc code=start
# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1) as SecondHighestSalary
#FROM Employee

/*
上面程式等同於：
SELECT IFNULL(
    (
    ...
    ), NULL) as ...

意思是上面那個程式會自動判斷，如果沒有SELECT到東西，就自動輸出NULL。
後面不能加FROM噢！（我也不清楚為什麼..）
*/

-- @lc code=end

