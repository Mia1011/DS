--
-- @lc app=leetcode id=1321 lang=mysql
--
-- [1321] Restaurant Growth
--

-- @lc code=start
# Write your MySQL query statement below
SELECT visited_on, (
    SELECT sum(amount)
    FROM Customer
    WHERE visited_on between adddate(c.visited_on, -6) and c.visited_on
    ) as amount, (
    SELECT round(sum(amount)/7, 2)
    FROM Customer
    WHERE visited_on between adddate(c.visited_on, -6) and c.visited_on 
    ) as average_amount
FROM Customer c
WHERE visited_on >= (
    SELECT adddate(min(visited_on), 6)
    FROM Customer
)
GROUP BY visited_on

# between 小 and 大

-- @lc code=end

