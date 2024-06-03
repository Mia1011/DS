--
-- @lc app=leetcode id=1251 lang=mysql
--
-- [1251] Average Selling Price
--

-- @lc code=start
# Write your MySQL query statement below
SELECT p.product_id, ifnull(round(sum(p.price*u.units)/sum(u.units), 2), 0) average_price
FROM  Prices p
LEFT JOIN UnitsSold u 
ON p.product_id = u.product_id 
AND u.purchase_date BETWEEN p.start_date and end_date
GROUP BY p.product_id
-- @lc code=end

