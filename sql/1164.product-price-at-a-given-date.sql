--
-- @lc app=leetcode id=1164 lang=mysql
--
-- [1164] Product Price at a Given Date
--

-- @lc code=start
# Write your MySQL query statement below
SELECT product_id, new_price as price
FROM Products
WHERE(product_id, change_date) in (
    SELECT product_id, max(change_date)
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
UNION

SELECT distinct product_id, 10 as price
FROM Products
WHERE(product_id) not in (
    SELECT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
)
-- @lc code=end

