--
-- @lc app=leetcode id=1068 lang=mysql
--
-- [1068] Product Sales Analysis I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT P.product_name, S.year, S.price
FROM Sales S
LEFT JOIN Product P ON S.product_id = P.product_id;
-- @lc code=end

