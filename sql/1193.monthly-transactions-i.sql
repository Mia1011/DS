--
-- @lc app=leetcode id=1193 lang=mysql
--
-- [1193] Monthly Transactions I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT date_format(trans_date, "%Y-%m") as month,  # substr(trans_date, 1, 7)
    country, 
    count(*) as trans_count, 
    sum(case when state="approved" then 1 else 0 end) as approved_count, 
    sum(amount) as trans_total_amount, 
    sum(case when state="approved" then amount else 0 end) as approved_total_amount
FROM Transactions
GROUP BY month, country

# numeric_function(case when...)

-- @lc code=end

