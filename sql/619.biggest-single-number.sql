--
-- @lc app=leetcode id=619 lang=mysql
--
-- [619] Biggest Single Number
--

-- @lc code=start
# Write your MySQL query statement below
SELECT max(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING count(num) = 1
) AS unique_numbers;

# FROM 後面還可以放一個程式！
-- @lc code=end

