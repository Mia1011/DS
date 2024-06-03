--
-- @lc app=leetcode id=1045 lang=mysql
--
-- [1045] Customers Who Bought All Products
--

-- @lc code=start
# Write your MySQL query statement below
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING count(distinct product_key) = (SELECT count(product_key) FROM Product)

# A FOREIGN KEY is a field in one table “among” the PRIMARY KEY in another table
# 所以只要數數量就好！

-- @lc code=end

