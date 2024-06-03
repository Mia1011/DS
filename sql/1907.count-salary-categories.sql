--
-- @lc app=leetcode id=1907 lang=mysql
--
-- [1907] Count Salary Categories
--

-- @lc code=start
# Write your MySQL query statement below
/*
SELECT 
    CASE 
        WHEN income < 20000 THEN "Low Salary"
        WHEN income > 50000 THEN "High Salary"
        ELSE "Average Salary"
    END AS category, count(*) AS accounts_count
FROM Accounts
GROUP BY category
 
# GROUP BY 後無法顯示 sum=0 的值...
*/ 

SELECT "Low Salary" as category, count(*) as accounts_count
FROM Accounts
WHERE income < 20000

UNION

SELECT "Average Salary" as category, count(*) as accounts_count
FROM Accounts
WHERE income >= 20000 AND income <= 50000

UNION

SELECT "High Salary" as category, count(*) as accounts_count
FROM Accounts
WHERE income > 50000

-- @lc code=end

