--
-- @lc app=leetcode id=1327 lang=mysql
--
-- [1327] List the Products Ordered in a Period
--

-- @lc code=start
# Write your MySQL query statement below
SELECT product_name, sum(unit) as unit
FROM Products
JOIN Orders USING(product_id)
WHERE extract(year_month FROM order_date) = "202002"
GROUP BY product_name
HAVING sum(unit) >= 100
-- @lc code=end

