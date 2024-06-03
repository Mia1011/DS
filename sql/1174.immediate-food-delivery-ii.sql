--
-- @lc app=leetcode id=1174 lang=mysql
--
-- [1174] Immediate Food Delivery II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT round(avg(order_date=customer_pref_delivery_date)*100, 2) as immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) in (
    SELECT customer_id, min(order_date)
    FROM Delivery
    GROUP BY customer_id
)
-- @lc code=end

